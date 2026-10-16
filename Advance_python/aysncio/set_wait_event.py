"""it is used to simply quick setting up event loop"""
import asyncio
from time import sleep


async def fetching(new_event):
    print("waitng for gathering")
    await new_event.wait()
    print("gathering done")


async def gathering(new_event):
    print("gathering")
    await asyncio.sleep(5)
    new_event.set()
    print("done gathering")


async def main():
    new_event = asyncio.Event()
    await asyncio.gather(fetching(new_event), gathering(new_event),)

asyncio.run(main())