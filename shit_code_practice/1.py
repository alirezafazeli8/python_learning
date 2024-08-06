# int_var = 1
# float_var = 1.5
# str_var = "alireza"
# list_var_names = ["alireza", "sara", "mohsen"]
# dict_var_user = {"name": "alireza", "lastname": "fazeli", "age": 19, "id": 2345}
# tuple_var_names = ("alireza", "sara", "mohsen")
# set_var_names = {1, 1, 2, 3, 4, 7, 6, 2, 5}

# set_var_names[0] = 0
# print(set_var_names)

# tuple_var_names[0] = "reza"

# print(tuple_var_names[0])

# for item in tuple_var_names:
#     print(item)

# print(dict_var_user)

# for key, value in dict_var_user.items():
#     print(
#         f"""
#           {key} : {value}

#           """
#     )

# print(8 % 5)

# print(6 / 4)
# print(6 // 3.7)

# print(round(3.7))
# print(round(3.5))
# print(round(3.4))

# print(round(3.7))
# print(round(3.7))
# print(round(3.7))
# print(abs(+45))
# print(abs(-45))
# # print(abs(5.5555555555555555555))
# print(abs(3 + 5j))

# my_number = 3.5
# print(my_number)
# my_number = int(my_number)

# print(type(my_number))
# print(my_number)

# print(float("8"))

# const dadad

# constant variable
# USERID = 453435

# expression_value = 2 * 2
# print(f"exp value : {expression_value}")

# get_user_salary = float(input("Pleas Enter Your Salary : "))
# tax = 0.1
# calculate_tax = tax * get_user_salary
# gov_msg = f"""
#     in the name of god.

#     dear citizen.
#     your salary is : ${get_user_salary} .
#     you should pay to us : ${calculate_tax:.2f} .

#     god bless you.

# """
# print(gov_msg)

# username = "alireza"
# USER_ID = 31
# msg = "username : " + username + " user id : " + str(USER_ID)

# print(msg)

# msg = "hi \n my name is \t alireza fazeli . this char : \\"
# name = " ali "

# print(len(msg))
# print(len(name))

# nums = [1, 2, 3, 4, 5]
# print(len(nums))

# name = "Alireza Fazeli"
# print(name[::-1])
# name[0] = "b"
# print(name)
# name = list(name)
# name[0] = "b"
# name = "".join(name)

# print(name)

# username = "alireza"
# user_id = 31
# age = 19

# # msg = "username : {} | userid : {} | age : {} ".format(username, age, None)

# # print(msg)
# print(username.upper())
# print(username.lower())
# print(username.capitalize())

# text = "Your name is alireza fazeli. how are you alireza."

# # print(text.find("alireza", 14))


# print(text.replace("a", "❤️"))

# user_year = int(input("your birth : "))
# calc_age = 2024 - user_year
# print(f"You Have {calc_age} years old .")

# print("❤️" * 100)


# shopping_card = ["book", "pen", "pencil", "glasses", "keyboard", "Mouse", "Monitor"]

# shopping_card_two = shopping_card
# shopping_card_two[0] = "null"

# print(shopping_card)

# matrix = [[1, 1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1, 1]]

# for layer_one in matrix:
#     for item in layer_one:
#         if item:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n", end="")


# shopping_card = [
#     "book",
#     "pen",
#     "pencil",
#     "glasses",
#     "pen",
#     "keyboard",
#     "Mouse",
#     "Monitor",
# ]

# new_items = ["iphone", "samsung"]

# shopping_card.append("airpod")
# shopping_card.insert(-1, "applewatch")

# shopping_card.extend(new_items)
# shopping_card.pop(2)
# shopping_card.remove("Mouse")

# print(shopping_card)

# shopping_card = [
#     "book",
#     "pen",
#     "pencil",
#     "glasses",
#     "pen",
#     "keyboard",
#     "Mouse",
#     "Monitor",
# ]


# print(
#     shopping_card[
#         shopping_card.index(
#             "pen",
#             2,
#         )
#     ]
# )

# print(shopping_card.count("pen"))
# shopping_card.sort()
# sorted_shopping_card = sorted(shopping_card)
# new_shoping = shopping_card.copy()

# print(shopping_card)
# new_shoping[0] = "apple"
# print(shopping_card)
# print(new_shoping)
# new_shoping.reverse()
# print(new_shoping)


# shopping_card = [
#     "book",
#     "pen",
#     "pencil",
#     "glasses",
#     "pen",
#     "keyboard",
#     "Mouse",
#     "Monitor",
# ]

# for item in shopping_card:
#     if item == "none":
#         print(True)
#         break

# print("apple" in shopping_card)


# username, age, *ids, city, car = [
#     "alirezafazeli",
#     19,
#     92341124124,
#     4959521,
#     "neka",
#     "benz",
# ]

# print(ids)

# user_information = {
#     "username": "saman_ghodoos",
#     "firstname": "saman",
#     "email": "test@test.com",
#     "age": 22,
#     "followers": ["alireza", "reza", "trump"],
# }

# show_info = f"""

#     id : {user_information["username"]}
#     name : {user_information["firstname"]}
#     email : {user_information["email"]}
#     age : {user_information["age"]}

#     followers :
# """

# print(show_info, end="")

# for item in user_information["followers"]:
#     print(
#         "\t" + item,
#         end="\t",
#     )
#     if item is False:
#         print("salam")

# i = 0
# while i < len(user_information["followers"]):
#     print(
#         "\t" + user_information["followers"][i],
#         end="\t",
#     )

#     i += 1

#     if i == len(user_information):
#         print("\n")

# import random

# names = ["ali", "sara", "mohsen"]

# print(names[random.randint(0, len(names) - 1)])

# my_dict = {"a": 1, "b": 2, "a": 3}

# print(my_dict["a"])


# user_information = {
#     "username": "saman_ghodoos",
#     "firstname": "saman",
#     "email": "test@test.com",
#     "age": 22,
#     "followers": ["alireza", "reza", "trump"],
# }

# if not user_information["phone"]:
#     print("err")

# if not user_information.get("phone"):
#     print("not found")


# for item in user_information.keys():
#     print(item)

# print(user_information.values())

# print(user_information.items())

# # user_information.clear()
# # print(user_information)

# new_dict = user_information.copy()
# new_dict["username"] = "rock"
# print(user_information)
# print(new_dict)
# num = [1, 2]
# num.remove(2)
# print(num)

# user_information.pop("firstname")
# user_information.update({"phone": "5694"})
# print(user_information)

# print(user_information.get("phone", "i cant find phone"))

# manual_dict = dict(username="alireza", phone=3434, age=19)

# print(manual_dict)

# my_tuple = (1, 2, 3, 4, 3)
# # my_tuple[0] = 3
# print(my_tuple.count(3))
# print(my_tuple.index(3))

# my_set = {1, 2, 3, 4}
# my_set2 = {1, 2, 3}
# print(my_set.difference(my_set2))
# print(my_set2.difference(my_set))

# my_set.add(5)

# my_set2 = my_set.copy()
# my_set2.add(8)

# my_set2.discard(8)

# my_set2.difference_update(my_set)

# print(my_set2)

# print(my_set.union(my_set2))
