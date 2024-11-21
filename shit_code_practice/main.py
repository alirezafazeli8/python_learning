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
# print("      a        ".strip())

# class Car:
#     # class object attribute
#     switch = True
    
#     def __init__(self, brand="BMW", model="AMG", color="BLACK", speed="250km"):
#         self.brand = brand
#         self.__model = model
#         self.color = color
#         # self.speed = speed
#         Car.speed = speed
        
#     def start(self):
#         if self.switch:
#             return f"{self.brand}:{self.__model} is started"
#         else: 
#             return "switch is off"
    
#     # @classmethod
#     # def can_drive(cls, age):
#     #     if age >= 18:
#     #         print("You can Drive with cars")
#     #     else:
#     #         print("You Cant Drive With Cars.")
    
#     @staticmethod
#     def can_drive(age):
#         if age >= 18:
#             print("You can Drive with cars")
#         else:
#             print("You Cant Drive With Cars.")
        

# car_one = Car()

# print(car_one.start())
# print(car_one.speed)

# Car.can_drive(15)


# class User:
#     def __init__(self, username, age):
#         if age >= 18:
#             self.username = username
#             self.age = age
#         else:
#             print("You Cant Play My Game.")
#     def sign_in(self):
#         print("User is Signed in.")
        
            
# class Wizard(User):
#     def __init__(self, username, wizard_name, ability):
#         User.username = username
#         self.wizard_name = wizard_name
#         self.ability = ability
        
#     def sign_in(self):
#         super().sign_in()
    
#         print(f"User {self.wizard_name} is signed in.")
    
#     def attack(self):
#         return f"{self.wizard_name} attakced with {self.ability}"


# class Archer(User):
#     def __init__(self, archer_name, ability):
#         self.archer_name = archer_name
#         self.ability = ability
        
#     def attack(self):
#         return f"{self.archer_name} attakced with {self.ability}"
        
        
        
# class Jungler(Wizard, Archer):
#     def __init__(self, username, wizard_name, ability):
#         Archer.__init__(self, wizard_name, ability)
#         Wizard.__init__(self, username, wizard_name, ability)


# jungler_one = Jungler("alirezafazeli", "Jungler", "speaking")

# print(jungler_one.attack())


# user_one = User("alirezafazeli", 18)
# wizard = Wizard(user_one.username, "Rocky", "Fire")
# # archer = Archer("Vexana", "arrows")

# print(wizard.username)

# print(dir(Wizard))

# class Toy:
    
#     names = ["benz", "bmw", "volvo"]
    
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
    
#     def __str__(self):
#         return "This is Specific Toy For Who Loves Car."
    
#     def __len__(self):
#         return 100
    
#     # def __del__(self):
#     #     print("Toy Is Deleted From Your Mind .")
        
#     def __call__(self, name):
#         return f"Your {name} toy is created ."
    
#     def __getitem__(self, i):
#         return self.names[i]
        
        
# toy_car = Toy("Car Toy", "red")

# # print(str(toy_car))
# # print(len(toy_car))

# # del toy_car

# # print(Toy("knife", "black"))
# print(toy_car("knife"))
# print(toy_car[1])


# print(issubclass(Toy, User))

# num_one = 10

# def multiple(num):
#     return num * 2

# print(multiple(2))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for i, num in enumerate(numbers):
# #     numbers[i] = num * 2
    
# # print(numbers)


# # numbers = list(map(lambda i: i  *2, numbers))
# numbers = list(filter(lambda i: i % 2 == 0, numbers))
# print(numbers)

# from functools import reduce


# def reduce_func(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(reduce_func, numbers, 0))

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# a.sort(key=lambda key: key[1])

# print(a)

# letter = [char + "😊" for char in "alirezafazeli"]

# print(letter)

# letter_set = {char for char in "alirezafazeli"}

# simple_dict = {
#     "a": 1,
#     "b": 2
# }


# new_dict = {key:value**2 for key,value in simple_dict.items()}
# print(new_dict)


# def my_decorator(func):
#     def wrapper(name):
#         print("---------greeet----------")
        
#         print(func(name))
        
#         print("---------greeet----------")
        
#     return wrapper

# @my_decorator
# def greet(name):
#     return f"Hello {name}"

# greet("alireza")



# def timed(func):
#     def wrapper(range_num):
#         import time

#         start = time.time()
    
#         func(range_num)

#         end = time.time()

#         duration = end - start 

#         print(f"{duration:.3f}sec time taked")
    
#     return wrapper


# @timed
# def multiple_number(range_num):
#     for num in range(range_num):
#         num = num**num
#         print(num)
#         print()


# multiple_number(500)

# while True:
#     try:
#         age = int(input("Enter Age  : "))
#         print(f"You are {age}")
#     except:
#         print("Pleas Enter Number Bro.")
#     else:
#         break

try:
    age = int(input("Enter Age  : "))
    if age < 18:
        raise ValueError("You are less then 18")
    else: 
        print(f"You are born in {2024 / age }")
    
except ValueError as vl_err:
    print(f"Pleas Enter INT | {vl_err}")
except ZeroDivisionError:
    print("Pleas Enter Correct Age. Not Zero.")
except:
    print("You Got error")
else:
    print("GoodLuck")
finally:
    print("Finally is everywhere")

