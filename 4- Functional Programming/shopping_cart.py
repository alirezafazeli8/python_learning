from functools import reduce


shopping_cart = [
    {"name": "laptop", "price": "1000", "count": "1"},
    {"name": "book", "price": "10", "count": "2"},
    {"name": "milk", "price": "2", "count": "5"},
]


def calc_amount(acc, item):
    calc = int(item["price"]) * int(item["count"])
    acc += calc
    return acc


amount = reduce(calc_amount, shopping_cart, 0)


print(f"Total Pay : {amount}$")
