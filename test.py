import asyncio
import logging

from sungrowinverter import SungrowInverter


_LOGGING = logging.getLogger(__name__)
_LOGGING.setLevel(logging.INFO)

client = SungrowInverter("192.168.1.127")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
result = loop.run_until_complete(client.async_update())

#Get a list data returned from the inverter.
print(client.data)