from collections import Counter, OrderedDict, defaultdict

# names = [
#     "alireza",
#     "sara",
#     "mahya",
#     "alireza",
#     "mahya",
#     "mahya",
#     "javad",
#     "ali",
#     "javad",
# ]


# print(Counter(names))

# users = {
#     "alireza": "1234",
#     "mahya": "1234",
#     "sara": "1234",
#     "javad": "1234",
#     "ali": "1234",
#     "amir": "1234",
# }


# new_names = defaultdict(lambda: "not found", users)

# print(new_names["kourosh"])


# dict1 = OrderedDict({"a": 1, "b": 2})
# dict2 = OrderedDict({"b": 2, "a": 1})

# print(dict1 == dict2)


# import datetime
# import time

# print(datetime.datetime.today())
# print(datetime.date.fromtimestamp(time.time()))
# print(datetime.time.tzname(datetime.datetime.today()))


import time
from array import array


def show_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("------------")
        func(*args, **kwargs)

        stop_time = time.time()

        print(f"time : {stop_time - start_time}")
        print("------------")

    return wrapper


@show_time
def show_item(item_iter):
    for item in item_iter:
        print(item)


array_item = array("i", [item for item in range(1000)])
list_item = [item for item in range(1000)]

# print(list_item)

show_item(list_item)
print("------------------------------")
show_item(array_item)
