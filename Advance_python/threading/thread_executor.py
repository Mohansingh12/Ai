import concurrent.futures
import time


def test(seconds):
    time.sleep(seconds)
    return 'done'

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    f1 = executor.submit(test,2)
    f2 = executor.submit(test,1)
    print(f1.result())
    print(f2.result())