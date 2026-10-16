import asyncio
import time


async def function(await_time,data):
    print(await_time)
    await asyncio.sleep(await_time)
    return data

async def main():
    task1 = function(3,'mohan')
    task2 = function(2,'sumit')
    result = await task1
    print(result)
    result = await task2
    print(result)

asyncio.run(main())