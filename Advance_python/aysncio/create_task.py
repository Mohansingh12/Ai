"""we use this function to run task simultaneously to improve effeminacy and to decrease ideal time"""

import asyncio



async def performing_task(time_taken, task):
    await asyncio.sleep(time_taken)
    print(task)

async def main():
    task1=asyncio.create_task(performing_task(time_taken=3,task='fecthing data'))
    task2=asyncio.create_task(performing_task(time_taken=4,task='loading defult data'))
    task3=asyncio.create_task(performing_task(time_taken=2,task='loading user information'))

    result1=await task1
    result2=await task2
    result3=await task3


asyncio.run(main())

"""this show that even the task load last finished first"""