import argparse
import asyncio
import logging
import sys

from . import __version__
from .ble import scan as ble_scan
from .ble import select_device_by_name
from .config import get_config_path, load_config, save_config
from .relay import BleRelay
from .server import run_tcp_server


logger = logging.getLogger("btstats")


def _configure_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s %(message)s")


def _print_devices(devices):
    for d in devices:
        name = d.name or "(unknown)"
        rssi = "" if d.rssi is None else f" rssi={d.rssi}"
        print(f"{name} {d.address}{rssi}")


def _get_config(args):
    path = get_config_path(args.config)
    return path, load_config(path)


def _cmd_show_config(args):
    path, _ = _get_config(args)
    print(path)
    return 0


def _cmd_scan(args):
    devices = asyncio.run(ble_scan(timeout=args.timeout))
    _print_devices(devices)
    return 0


def _select_device(args):
    if args.device:
        return args.device, None
    if args.name:
        device = asyncio.run(select_device_by_name(args.name, timeout=args.timeout))
        if not device:
            raise RuntimeError(f"No device named {args.name!r} found")
        return device.address, device.name
    raise RuntimeError("Provide --device or --name")


def _cmd_connect(args):
    path, doc = _get_config(args)
    address, name = _select_device(args)
    doc["bluetooth"]["address"] = address
    if name:
        doc["bluetooth"]["name"] = name
    if args.char_uuid:
        doc["bluetooth"]["characteristic_uuid"] = args.char_uuid
    if args.port:
        doc["server"]["port"] = args.port
    save_config(doc, path)
    print(f"Saved device {address} to {path}")
    return 0


async def _serve(args):
    path, doc = _get_config(args)
    address = args.device or doc["bluetooth"]["address"]
    if not address:
        raise RuntimeError("No Bluetooth address configured. Run connect first.")
    char_uuid = args.char_uuid or doc["bluetooth"]["characteristic_uuid"] or None
    port = args.port or int(doc["server"]["port"])
    relay = BleRelay(address=address, characteristic_uuid=char_uuid)
    await relay.start()

    async def on_gauge(gauge):
        await relay.send(gauge)

    logger.info("Starting TCP server on port %s", port)
    await run_tcp_server(host=args.host, port=port, on_gauge=on_gauge)


def _cmd_serve(args):
    asyncio.run(_serve(args))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="btstats")
    parser.add_argument("--config", help="Path to config TOML")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging")
    parser.add_argument("--version", action="version", version=f"btstats {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    show_config = sub.add_parser("show-config", help="Show config path")
    show_config.set_defaults(func=_cmd_show_config)

    scan = sub.add_parser("scan", help="Scan BLE devices")
    scan.add_argument("--timeout", type=float, default=5.0)
    scan.set_defaults(func=_cmd_scan)

    connect = sub.add_parser("connect", help="Save device info to config")
    connect.add_argument("--device", help="BLE address")
    connect.add_argument("--name", help="BLE device name")
    connect.add_argument("--char-uuid", help="Preferred characteristic UUID")
    connect.add_argument("--port", type=int, help="Local server port")
    connect.add_argument("--timeout", type=float, default=5.0)
    connect.set_defaults(func=_cmd_connect)

    serve = sub.add_parser("serve", help="Run TCP server and relay to BLE")
    serve.add_argument("--device", help="BLE address override")
    serve.add_argument("--char-uuid", help="Characteristic UUID override")
    serve.add_argument("--port", type=int, help="Local server port")
    serve.add_argument("--host", default="127.0.0.1", help="Bind host")
    serve.set_defaults(func=_cmd_serve)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    _configure_logging(args.verbose)
    try:
        return args.func(args)
    except Exception as exc:
        logger.error("%s", exc)
        return 2


if __name__ == "__main__":
    sys.exit(main())
