# def my_gen():
#     yield 1
#     yield 2
#     yield 3


# g = my_gen()

# next(g)
# next(g)

# print(next(g))


# def counter_gen(max_value):

#     count_num = 1
#     while count_num <= max_value:
#         yield count_num
#         count_num += 1


# count = counter_gen(10)

# for num in count:
#     print(num)


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# fib_gen = fibonacci()
# for _ in range(10):
#     print(next(fib_gen))


# class Multiple:

#     number = 1

#     def __init__(self, num):
#         self.num = num

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.number <= self.num:
#             self.number += self.number * 2
#             return self.number
#         else:
#             raise StopIteration


# my_num = Multiple(20)

# for item in my_num:
#     print(item)


# def get_num(num):
#     for i in range(num):
#         yield i


# gen_num_var = get_num(5)

# next(gen_num_var)
# next(gen_num_var)
# next(gen_num_var)

# print(gen_num_var)


# class MySchool:
#     def __init__(self, name, management, classes):
#         self.name = name
#         self.management = management
#         self.classes = classes
#         self.count = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.count += 1
#         list_attr = list(vars(self).values())
#         return list_attr[self.count]


# my_school = MySchool("shahed", "salehi", 32)

# print(next(my_school))
# print(next(my_school))
# print(next(my_school))
# print(next(my_school))
# print(next(my_school))


# class NumGen:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.curr = first - 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.curr += 1
#         if self.curr == self.last:
#             raise StopIteration
#         else:
#             return self.curr


# for item in NumGen(5, 10):
#     print(item)


# def gen_number(num):
#     for i in range(num):
#         yield i


# my_number = gen_number(10)

# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))
# print(next(my_number))


# list1 = iter([1, 2, 3])

# print(next(list1))


# ---------- Own Generator ---------
class num_generators:
    def __init__(self, num):
        self.num = num

        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count < self.num:
            self.count += 1
            return self.count
        else:
            raise StopIteration


my_num = num_generators(10)

print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
