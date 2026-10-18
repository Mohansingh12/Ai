"""this is concept used for preventing two threading access same memory at the same time"""


import threading

counter=0
counter_lock = threading.Lock()

def task1():
    global counter
    with counter_lock:
        counter+=1
        print(counter)
def main():
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task1)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(counter)

if __name__ == '__main__':
    main()