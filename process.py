"""
скрипт для демонстрации процессов
"""
import os
import subprocess
import multiprocessing as mp
import time
def _start():
    print('start')
    #print(f"{os.getpid()}")
    #print(f"{os.getppid()}")

    process = mp.Process(target=welcome, args=("welcome",))
    process.start()
    process.join()
    print(process.name)
    print(process.is_alive())


def welcome(message):
    print(message)
    time.sleep(5)
    work()

def work():
    print('work')
    finish()

def finish():
    print('finish')

_start()
