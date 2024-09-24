# my_file = open("./test.txt")

# print(my_file.read())
# my_file.seek(3)
# print(my_file.read())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())
# my_file.close()

# with open("./test.txt", mode="r+") as my_file:
#     for i in range(10):
#         my_file.write(f"{i + 1}\n")


# with open("./test.txt", mode="a") as my_file:
#     for i in range(20, 30):
#         my_file.write(f"{i + 1}\n")


# with open("./test.txt", mode="w") as my_file:
#     for i in range(20, 30):
#         my_file.write(f"{i + 1}\n")


try:
    with open("./sad.txt", mode="r") as my_file:
        for i in range(20, 30):
            my_file.write(f"{i + 1}\n")
except FileNotFoundError:
    print("File Not Found")
except IOError:
    print("Operation is failed")
