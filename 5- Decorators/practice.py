# def greet(func):
#     def wrapped_func(name):
#         print("------ Welcome ------")
#         print(name)
#         func(name)
#         print("------GoodBye--------")

#     return wrapped_func


# @greet
# def say_hello(name):
#     print("Hello !")


# # greet(say_hello)

# say_hello("alireza")


# def my_decorator_func(func):
#     def wrapper(*args, **kwargs):
#         print("------wrapper------")
#         print(kwargs)
#         print(args[0])
#         func(*args, **kwargs)
#         print("------wrapper------")

#     return wrapper


# @my_decorator_func
# def hello(*args, **kwargs):
#     print("hello world")


# hello("alireza", name="mahya", num="sara")

import time


def performance(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        sum = stop_time - start_time
        print(f"its taked {sum:4f}")

    return wrapper


@performance
def calc():
    for item in range(100):
        item**2


calc()
