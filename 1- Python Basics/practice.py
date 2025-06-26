# data types

# int_data = 34
# float_data = 34.5
# string = "Hello"
# string2 = "hello"
# name_list = ["alireza", "sassan", "javad"]
# user_info = {
#     "username": "alirezafazeli",
#     "email": "test@test.com",
#     "age": 20,
#     "friends": ["amir", "javad"],
# }

# tuple_data = (1, 2, 3, 4, 5)
# set_data = {1, 2, 3, 4, 5}
# bool_data = True

# print(12 % 5)

# print(6 // 4.2)

# print(round(3.2))
# print(round(3.5))
# print(round(3.6))
# print(round(3.9))


# print(abs(-1))
# print(abs(+1))


# USER_ID = 5645435
# username = "alireza"

# USER_ID = 0

# print(USER_ID)


# Mini project calculate tax :

# user_income = int(input("Pleas Enter Your Income : "))

# tax = 0.02
# calculate_tax = user_income * tax

# print(f"You Should Pay : {calculate_tax}")

# value = 8

# # value += 8
# # value *= 8
# # value /= 2
# value **= 2

# print(value)


# user_name = "alireza"
# user_id = 23

# msg = "Hello " + user_name + " Your ID is : " + str(user_id)

# print(msg)


# print("\tHello \\n my name is alireza fazeli")


# text = "Thisis new text"

# print(text[-4::])

# text[0] = "H"


# user_name = "alireza"
# user_id = 35364

# msg = "username : {} user id : {}".format(user_name, user_id)


# print(msg)


# upper_text = "ALIREZA"
# lower_text = "saman"
# text = "hello my name is alireza fazeli"

# print(upper_text.lower())
# print(upper_text.upper())
# print(lower_text.capitalize())

# print(upper_text.find("A", 1))

# text = text.replace("hello", "hi")
# print(text)


# mini project | calculate the age

# user_age = int(input("Pleas Enter Your birth : "))

# year = 2025
# calculate = year - user_age

# print(f"You are  {calculate}")

# Mini Project  : Password Checker
# user_password = input("Pleas Enter Your Password : ")

# hide_pass = len(user_password) * "*"

# print(f"Youre Password is {hide_pass}")

# user_names = ["alireza", "javad", "amir", "hassan", "ali", "mohammad"]
# user_ages = [1, 2, 2, 3, 4, 5]


# # print(len(user_names))
# user_names.append("asghar")
# user_names.insert(2, "hatef")

# user_names.extend(user_ages)

# user_names.pop()
# user_names.remove(2)
# user_names.clear()

# # print(user_names)
# print(user_names)


# numbers = [1, 2, 3, 4, 5, 2, 6, 7, 8, 2, 9, 10]

# # print(numbers.index(2, 3))
# # print(numbers.count(2))

# new_number = sorted(numbers)
# new_number.reverse()


# print(new_number)
# text = "hello my name is alireza fazeli"
# user_info = {"name": "alireza", "age": 20}
# users = ["alireza", "javad", "amir", "hassan", "ali", "mohammad"]


# print("name" in text)
# print("isss" in text)
# print("name" in user_info)


# alireza, javad, *other, mohammad = [
#     "alireza",
#     "javad",
#     "amir",
#     "hassan",
#     "ali",
#     "mohammad",
# ]


# print(alireza, javad, other, mohammad)


# user_info = {
#     "username": "alirezaJKA",
#     "name": "alireza",
#     "age": 20,
# }

# # print(user_info["friends"])
# # print(user_info.get("friends"))
# print(user_info.keys())
# print(user_info.values())
# print(user_info.items())


# for key, value in user_info.items():
#     print(f"added+{key}-{value} to server.")

# user_info.clear()

# print(user_info)


# user_info.pop("name")
# user_info.popitem()
# user_info.update({"phone_number": 5545465})
# print(user_info)

# user_info = dict(name="alireza", last_name="fazeli", age=20)

# print(user_info)


# numbers = (1, 2, 3, 4, 3, 3, 5)

# # numbers[0] = 2


# print(numbers.count(3))


# my_tuple = (1, 2, 3, 2, 2, 2, 6, 3)

# # ordered
# print(my_tuple[0])
# print(my_tuple[5])

# print(my_tuple)

# # any objects should be unique
# my_set = {1, 2, 3, 2, 2, 2, 6, 3}

# print(my_set)

# # print(my_set[0])
# # print(my_set[5])

# # for item in my_set:
# #     print(my_set)

# my_set.add("alireza")
# my_set.add("alireza")


# print(my_set)


set_one = {
    1,
    2,
    3,
}
set_two = {4, 5, 6, 7, 8, 9}

# set_two.discard(9)

# print(set_one.difference(set_two))
# print(set_two)
# set_one.difference_update(set_two)

# print(set_one.intersection(set_two))
# print(set_one.isdisjoint(set_two))

set_three = set_one.union(set_two)

print(set_three)
