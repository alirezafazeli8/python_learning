def main():

    import utility

    # import package
    # import shop.shopping_card
    from shop import shopping_card
    from shop.order.order import order
    from shop.order.order_food import order_food, food_speed, max

    # using module
    print(utility.divide(6, 2))
    print(utility.multiple(6, 2))

    shopping_card.buy("apple", "orange", "banana")

    order("sabzi")
    order_food("hamburger")
    food_speed(5)
    max()


def say_hello():
    print("hello")


if __name__ == "__main__":
    main()

# print(dir(utility))
