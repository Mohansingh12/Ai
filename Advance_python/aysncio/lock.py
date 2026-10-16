"""use to prevent working on a same file or resource so that it await for the last task to finsh first"""
import asyncio

lock = asyncio.Lock()

async def resource_handling(name_task):
    global lock
    async with lock:
        print(f"task is running {name_task}")
        await asyncio.sleep(5)
        print(f"task is done {name_task}")
async def main():
    task1 = asyncio.create_task(resource_handling('addition'))
    task2 = asyncio.create_task(resource_handling('multiply'))

    await asyncio.gather(task1, task2)


asyncio.run(main())