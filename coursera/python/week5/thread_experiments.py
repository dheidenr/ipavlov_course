import time
import os
import threading

from multiprocessing import Process

# pid = os.getpid()

# pid = os.fork()


def thread_one():
    for _ in range(3):
        # print("child:", os.getpid())
        print("child: ", threading.currentThread().getName() + '\n')
        time.sleep(2)


def thread_two():
    for _ in range(3):
        # print("parent", os.getpid())
        print("parent:", threading.currentThread().getName() + '\n')
        time.sleep(2)

def doubler(number):
    """
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    time.sleep(2)
    print()


if __name__ == "__main__":
    # for i in range(5):
    #     my_thread = threading.Thread(target=thread_one)
    #     my_thread.start()
    #     no_my_thread = threading.Thread(target=thread_two)
    #     no_my_thread.start()
    #     # my_thread = threading.Thread(target=thread_two(), args=(i,))
    #     # my_thread.start()

    proc_one = Process(target=thread_one(), )
    proc_two = Process(target=thread_two())


    proc_one.start()  # Стартовать процесс
    proc_two.start()

    proc_one.join()  # Ждать пока процесс завершиться
    proc_two.join()
