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


class Multiple:

    number = 1

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):

        if self.number <= self.num:
            self.number += self.number * 2
            return self.number
        else:
            raise StopIteration


my_num = Multiple(20)

for item in my_num:
    print(item)
