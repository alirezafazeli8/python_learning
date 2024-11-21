import time
import math


def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()

        sum_time = finish_time - start_time

        print(f"{func.__name__} | {round(sum_time, 2)}")

    return wrapper


@calculate_time
def greet():
    time.sleep(2)
    print("hello")


greet()
