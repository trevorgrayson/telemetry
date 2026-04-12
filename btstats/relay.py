import asyncio
import logging

from .ble import connect, find_writable_characteristic, safe_disconnect, write_gauge


logger = logging.getLogger("btstats")


class BleRelay:
    def __init__(self, address, characteristic_uuid=None, reconnect_delay=2.0):
        self.address = address
        self.characteristic_uuid = characteristic_uuid
        self.reconnect_delay = reconnect_delay
        self.queue = asyncio.Queue()
        self._task = None
        self._stop_event = asyncio.Event()

    async def start(self):
        if self._task:
            return
        self._task = asyncio.create_task(self._run())

    async def stop(self):
        self._stop_event.set()
        if self._task:
            await self._task

    async def send(self, gauge_message):
        await self.queue.put(gauge_message)

    async def _run(self):
        while not self._stop_event.is_set():
            client = None
            try:
                logger.info("Connecting to %s", self.address)
                client = await connect(self.address)
                char_uuid = await find_writable_characteristic(
                    client, preferred_uuid=self.characteristic_uuid
                )
                if not char_uuid:
                    raise RuntimeError("No writable characteristic found")
                logger.info("Using characteristic %s", char_uuid)
                while not self._stop_event.is_set():
                    gauge = await self.queue.get()
                    payload = f"{gauge.name}:{gauge.value}|g".encode("utf-8")
                    await write_gauge(client, char_uuid, payload)
                    self.queue.task_done()
            except Exception as exc:
                logger.warning("BLE relay error: %s", exc)
                await asyncio.sleep(self.reconnect_delay)
            finally:
                if client:
                    await safe_disconnect(client)
