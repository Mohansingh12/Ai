"""this program show that how to use aysncio and where"""
import asyncio
from asyncio import events
from itertools import cycle


async def fetching_info(id,cycle):
    print(f'fetching_info:{id}')
    await asyncio.sleep(1)
    cycle.set()
    print(f'fetched_info:{id}')
    await asyncio.sleep(1)
async def loading_info():
    print('showing_info')
    await asyncio.sleep(1)

async def storing_info(cycle):
    await cycle.wait()
    print('storing_info')

async def main():
    cycle= asyncio.Event()
    req= fetching_info(id,cycle)
    display= loading_info()
    store= storing_info(cycle)

    await asyncio.gather(req, display, store)


asyncio.run(main())

