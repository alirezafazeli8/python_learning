# my_list = range(1, 11)
# my_list_2 = []

# for item in my_list:
#     my_list_2.append(item * 2)

# print(my_list_2)

# ------- map----------

# def my_func(item):
#     return item * 2


# my_list = list(map(my_func, range(1, 11)))


# print(my_list)


# ---------- filter ----------


# def my_filter(item):
#     if item["license"] == True:
#         return True


# filter_items = list(
#     filter(
#         my_filter,
#         [
#             {"name": "alireza", "license": True},
#             {"name": "sara", "license": False},
#             {"name": "mahya", "license": True},
#         ],
#     )
# )


# print(filter_items)


# -------- zip -------


names = ["alireza", "mahya", "javad"]
last_names = ["fazeli", "ghaderi", "dehghan"]

print(list(zip(names, last_names)))
