import utility

# import package
# import shop.shopping_card
from shop import shopping_card
from shop.order.order import order
from shop.order.order_food import order_food, food_speed, max

# using module
print(utility.divide(6, 2))
print(utility.multiple(6, 2))

# print(shop.shopping_card)

# buy module from shop package
# shop.shopping_card.buy("apple", "orange", "banana")
shopping_card.buy("apple", "orange", "banana")

order("sabzi")
order_food("hamburger")
food_speed(5)
max()

if __name__ == "__main__":
    pass

# print(dir(utility))
