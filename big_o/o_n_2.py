my_name = ["alireza"]
books = ["sara", "javad", "ali", "mohsen", "reza", "jamil", "alireza"]


def find_name(books, my_name):
    for book in books:
        for name in my_name:
            if book == name:
                print(True)
                break


find_name(books, my_name)
find_name([item for item in range(10000000)], [100000001])
