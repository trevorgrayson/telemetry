import asyncio

from .statsd import parse_gauge


async def _handle_client(reader, writer, on_gauge):
    try:
        while True:
            line = await reader.readline()
            if not line:
                break
            text = line.decode("utf-8", errors="replace").strip()
            if not text:
                continue
            gauge = parse_gauge(text)
            if not gauge:
                continue
            await on_gauge(gauge)
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            await asyncio.sleep(0)


async def run_tcp_server(host, port, on_gauge):
    server = await asyncio.start_server(
        lambda r, w: _handle_client(r, w, on_gauge), host, port
    )
    async with server:
        await server.serve_forever()
