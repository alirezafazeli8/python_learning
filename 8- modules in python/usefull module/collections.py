from collections import Counter, OrderedDict, defaultdict

dict1 = OrderedDict({"a": 1, "b": 2})
dict2 = OrderedDict({"a": 1, "b": 2})
dict3 = OrderedDict({"b": 2, "a": 1})

print(dict1 == dict2)
# Output :
# True

print(dict2 == dict3)
# Output :
# False

# user_info = defaultdict(
#     lambda: "عه عه پیدا نشد",
#     {"first_name": "alireza", "last_name": "fazeli", "age": 19},
# )

# print(user_info["phone"])

# # names = ["reza", "ali", "reza", "sara", "javad", "sara", "sara"]

# # sentence = "ja ja javad salam be be roye"

# # print(Counter(names))
# # print(Counter(sentence))


# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 2}

# print(dict1 == dict2)
# # Output :
# # True

# dict3 = {"b": 2, "a": 1}
# print(dict1 == dict3)
# # Output :
# # True
