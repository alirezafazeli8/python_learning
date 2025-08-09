# print(type(""))
# print(type(2))
# print(type([]))
# print(type({}))
# print(type(()))
# print(type(True))
# print(type(2.2))


# class BigObject:
#     pass


# obj_one = BigObject()
# obj_two = BigObject()


# print(print(obj_one))
# print(print(obj_two))


# class PlayerCharacter:
#     def __init__(self, name, ability):
#         self.name = name
#         self.ability = ability

#     def user_info(self):
#         return f"""
#                     Player Information :
#                     --------------------
#                     name : {self.name}
#                     ability : {self.ability}

#               """


# player_one = PlayerCharacter("alireza", "gun")
# player_two = PlayerCharacter("saman", "knife")

# print(player_one.ability)
# print(player_two.ability)

# print(player_one.user_info())
# print(player_two.user_info())

# player_one.age = 20

# print(player_one.age)


# class PlayerCharacter:
#     membership = True

#     def __init__(self, name="user", age=0):

#         if self.membership:
#             self.name = name
#             self.age = age
#         else:
#             print("Buy MemeberShip")

#     def run(self, run_num=0):
#         if PlayerCharacter.membership:
#             print(f"run number : {run_num}")
#         else:
#             print("Buy MemeberShip")


# user_one = PlayerCharacter("alireza", 20)
# user_one.run(50)


# user_two = PlayerCharacter()
# user_two.run()
# print(user_two.name)


# Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# def find_oldest_cat(*cats):
#     cat_age = []
#     cat_names = []

#     for cat in cats:
#         cat_age.append(cat.age)
#         cat_names.append(cat.name)

#     max_cat_age = cat_age.index(max(cat_age))

#     print(f"Oldes Cat is : {cat_names[max_cat_age]}")


# cat1 = Cat("jame", 25)
# cat2 = Cat("rahim", 2)
# cat3 = Cat("lara", 23)


# find_oldest_cat(cat1, cat2, cat3)
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def cat_shops(cls, city):
#         import random

#         print(f"You Have {random.randint(1, 5)} In {city}")


# Cat.cat_shops("Neka")
# Cat.cat_shops("Sari")


# class Car:
#     pass


# benz_car = Car()
# bmw_car = Car()

# print(type(benz_car))


# Harry Potter Game
# class PlayerCharters:
#     def __init__(self, name="player00", ability="empty"):
#         self.name = name
#         self.ability = ability

#     def run(self):
#         return f"{self.name} run now."


# player1 = PlayerCharters("Harry", "Knife")
# print(player1.name, player1.ability)
# print(player1.run())

# # --------------

# player2 = PlayerCharters()
# player2.money = 2000
# print(player2.name, player2.ability, player2.money)


# def test():
#     return


# print(test())


# class PlayerCharacter:
#     # class object attribute
#     membership = False

#     def __init__(self, name, ability):
#         if self.membership:
#             self.name = name
#             self.selah = ability
#         else:
#             print("Buy Membership ...")


# player1 = PlayerCharacter("alireza", "knife")
# player1.membership = True


class Dog:
    species = "Toole Sag"
    num_dog = 0

    def __init__(self, name):
        self.name = name

        Dog.num_dog += 1

    @classmethod
    def dog_sound(cls):
        print("Hop Hop")


dog1 = Dog("javad")
dog2 = Dog("max")
dog3 = Dog("hira")


print(Dog.num_dog)

Dog.dog_sound()
