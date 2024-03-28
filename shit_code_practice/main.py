# age = 18

# can_drive = ("You Can Drive With Car" if age >= 18 else "You Cant Drive")

# print(can_drive)

# print(not False)

# print(not(True))

# a = ["a", "b"]
# b = a 
# c = ["a", "b"]

# print(a == b)
# print(b == c)
# print(b is c)
# print(a is b)

# print(f"a : {id(a)}")
# print(f"b : {id(b)}")
# print(f"c : {id(c)}")


names = ["alireza", "sara", "mohsen", "javad"]
user_info  = {
    "name": "alireza",
    "last_name": "fazeli",
    "age": 19,
    "country": "IR",
    "Friends": ["ali", "mohammad", "javad"]
}

# for name in names:
#     print("")

#     for letter in name:
#         print(letter)


# for key, value in user_info.items():
#     print(key, value)


# print(user_info.items())

# num = 0

# while num <= 1000000000:
#     print(f"Hello World {num}")
    
#     num += 1

# for num in range(20, 0, -1):
    # print(num)

# for index, value in enumerate(names):
#     print(index, value)


# print()


# user_input = input("Enter : ")

# while int(user_input) != 1:
#     print("Enter Again")
#     user_input = input("Enter : ")
# else:
#     print("Correct !")

# while False:
#     pass
# else:
#     print("True")

# def my_func(**kwargs):
#     print(kwargs)
    
# my_func(name="alireza", last_name="fazeli")

# name = "alireza"

# if (length := len(name)) > 5:
#     print(f"its too long. len : {length}")


# total = 10

# def show_total():
#     global total
    
#     total += 1
#     return total
    

# print(show_total())

# print(total)

# -- dependency injection

# total = 10

# def show_total(total):
#     total += 1
#     return total
    
    
# print(show_total(show_total(show_total(show_total(total)))))


# def x():
#     a = 10
#     def y():
#         nonlocal a
#         a += 1
#         return a
#     return y()

# print(x())
print("      a        ".strip())