from shop.cart import add_to_cart
from shop.payment import proccess_payemnt

print(__name__)
add_to_cart("laptop")
proccess_payemnt("1000")


if __name__ == "__main__":
    print("Root Runned")
else:
    print("root runned ?")
