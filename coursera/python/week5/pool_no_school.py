# Пул потоков, cuncurrent.futures.Future
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time


def f(a):
    # for _ in range(3):
    #     time.sleep(2)
    #     print("potok", time.time())
    return a * a


# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())

