"""semaphore only allow the limited no of task to get the resource so the it doest put a lot of load that it cant handle"""
import asyncio


async def resource_handling(semaphore,task_name,time):
    async with semaphore:
        print(f'task in process{task_name}')
        await asyncio.sleep(time)
        print(f'task in done{task_name}')

async def main():
    semaphore = asyncio.Semaphore(2)
    task1 = asyncio.create_task(resource_handling(semaphore,'add',1))
    task2 = asyncio.create_task(resource_handling(semaphore,'mul',2))
    task3 = asyncio.create_task(resource_handling(semaphore,'sub',3))
    task4 = asyncio.create_task(resource_handling(semaphore,'mul',4))

    await asyncio.gather(task1,task2,task3,task4)


asyncio.run(main())