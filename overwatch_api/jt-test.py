import asyncio
import aiohttp

from overwatch_api.core import AsyncOWAPI
from overwatch_api.constants import *

async def testing(loop):
    # Instantiating the api
    client = AsyncOWAPI()
    data = {}

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:

        print('Fetching Profile......', end="")
        data[XBOX] = await client.get_profile("WokNinja", session=session, platform=XBOX)
        print('OK')
        print('Fetching Stats........', end="")
        data[XBOX] = await client.get_stats("WokNinja", session=session, platform=XBOX)
        print('OK')

    pprint_dict(data)

def pprint_dict(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pprint_dict(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing(loop))