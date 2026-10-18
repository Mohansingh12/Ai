import threading


def task1(task_id:int, result:str):
    print(f'this is a task1 {task_id}')

def task2(task_id:int, result:str):
    print(f'this is a task2 {task_id}')

t1=threading.Thread(target=task1,args=([1,'good']))
t2=threading.Thread(target=task2,args=([2,'bad']))


t1.start()
t2.start()
t1.join()
t2.join()

