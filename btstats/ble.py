import asyncio
from dataclasses import dataclass

from bleak import BleakClient, BleakScanner


@dataclass(frozen=True)
class DiscoveredDevice:
    name: str
    address: str
    rssi: int | None


def _is_writable(char):
    props = {p.lower() for p in getattr(char, "properties", [])}
    return "write" in props or "write-without-response" in props


def _match_name(device_name, target):
    if not device_name or not target:
        return False
    return device_name.lower() == target.lower()


async def scan(timeout=5.0):
    devices = await BleakScanner.discover(timeout=timeout)
    results = []
    for d in devices:
        results.append(DiscoveredDevice(name=d.name or "", address=d.address, rssi=0))
                                        # rssi=d.get_rssi()))
    return results


async def select_device_by_name(name, timeout=5.0):
    devices = await scan(timeout=timeout)
    for d in devices:
        if _match_name(d.name, name):
            return d
    return None


async def connect(address):
    client = BleakClient(address)
    await client.connect()
    return client


async def find_writable_characteristic(client, preferred_uuid=None):
    services = await client.get_services()
    if preferred_uuid:
        char = services.get_characteristic(preferred_uuid)
        if char and _is_writable(char):
            return char.uuid
        return None
    for service in services:
        for char in service.characteristics:
            if _is_writable(char):
                return char.uuid
    return None


async def write_gauge(client, characteristic_uuid, payload):
    await client.write_gatt_char(characteristic_uuid, payload, response=False)


async def safe_disconnect(client):
    try:
        await client.disconnect()
    except Exception:
        await asyncio.sleep(0)
