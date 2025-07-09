# print(bool(0))
# print(bool(None))
# print(bool(""))
# print(bool(""))
# print(bool(""""""))
# print(bool(()))
# print(bool({}))
# print(bool([]))


# Ternary Operator
# is_married = False

# check_married = "Yes" if is_married == True else "No"

# print(check_married)

# print(not "")


# var_1 = 1
# var_2 = 2
# var_3 = 0
# var_4 = None


# print(var_1 == var_2)
# print(var_3 == var_4)
# print(1 == 1.0)
# print(1 is 1.0)
# print([] == [])
# print([] is [])


# var_1 = []
# var_2 = [1, 2]
# var_3 = var_2

# print(var_2 == var_3)
# print(var_2 is var_3)

# print(id(var_2))
# print(id(var_3))

# for i in range(10, 0, -1):
#     print(i)

# names = ["alireza", "sassan", "javad", "mohammad", "ali", "hassan"]

# for num, name in enumerate(names):
#     print(f"{num}-{name}")


# i = 10

# while i > 0:
#     print(i)
#     i -= 1


# i = 0

# while i < 10:
#     print(i)
#     i += 1


# user_password = input("Pleas Enter Your Password : ")

# while user_password != "123":
#     print("incorrect")
#     user_password = input("Pleas Enter Your Password : ")
# else:
#     print("Correct, Welcome")

# while True:
#     user_password = input("pleas enter your password : ")

#     if user_password == "123":
#         print("welcome")
#         break
#     else:
#         print("incorrect")
#         continue


# def say_name():
#     pass


# print("alireza", end="")
# print("fazeli", end="")


# Mini Project  : Print Picture


# my_pic = [
#     [1, 1, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 1],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]


# def print_pic(pic, fill="*", empty=" "):

#     for line in pic:
#         print("")
#         for num in line:
#             if num == 1:
#                 print(fill, end="")
#             elif num == 0:
#                 print(empty, end="")


# print_pic(my_pic, fill="0", empty="-")

# duplicate exercise
# alphabet = ["a", "b", "c", "c", "b", "d", "e"]
# duplicate = []

# for alpha in alphabet:
#     if alphabet.count(alpha) > 1:
#         if alpha not in duplicate:
#             duplicate.append(alpha)


# print(duplicate)


# def say_hello():
#     """
#     this is say hello function

#     maded by alireza fazeli
#     """
#     print("hello")


# # say_hello()

# # print(help(say_hello))

# print(say_hello.__doc__)


# def super_func(*args):
#     print(args)


# super_func(1, 2, 3, 4, 5)


# def invite_users(*users):
#     for count, user in enumerate(users):
#         print(f"User {count}-{user} Invited to server")


# invite_users("alireza", "mohammad", "sara")


# def kwargs_func(**kwargs):
#     print(kwargs)


# kwargs_func(num1=1, num2=2, num3=3)


# API_KEY = 12345566


# def connect_api(username, **kwargs):
#     if "api_key" in kwargs:
#         print(f'{username} added with {kwargs["api_key"]} to database')
#     else:
#         raise ValueError("api key required")


# # connect_api("alirezfazeli", api_key=API_KEY)
# connect_api("saman")


# def test_func(username, *args, phone=None, **kwargs):
#     pass


# nums = {2, 10, 33, 0, 88, 1, 44, 67, 11, 99}
# alpha = ["a", "a", "b", "c", "c"]
# print(max(nums))
# print(min(nums))

# print(max(alpha))


# word = "alireza"

# if (max_word := len(word) ** 2) > 2:
#     print(max_word)

# if True:
#     x = 10


# print(x)

# x = 10


# def test():
#     global x

#     x += 2
#     print(x)


# test()

# while True:
#     x += 10
#     break


# x = 10


# def dep_injection(x):
#     x += 1
#     return x


# print(dep_injection(dep_injection(x)))


# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print(x)

#     inner()
#     print(x)


# outer()


# name = "            Alireza Fazeli       .      "

# print(name.strip())
