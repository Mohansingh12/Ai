"""it is a function the kills the thread as soon as main thread is done"""

import threading
import time

def task1():
    while True:
        print(time.time())
        time.sleep(1)

thread=threading.Thread(target=task1)
thread.daemon=True
thread.start()
time.sleep(4)
print(time.time())


