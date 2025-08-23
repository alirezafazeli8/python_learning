# try:
#     num_one = int(input("Enter Number : "))
#     sum = num_one**2
#     print(sum)
# except TypeError as typeerror:
#     print(f"Pleas Fix Input Number In Your Code ... || {typeerror}")
# except:
#     print("Error From Server...")
# else:
#     print("this is else")
# finally:
#     print("Application Stopped.")

while True:
    try:
        print("--Welcome To Alireza Bank--")
        user_id = input("Pleas Enter Your Bank ID : ")
        if not isinstance(int(user_id), int):
            raise TypeError("Pleas Enter Correct Number ID")
    except (TypeError, ValueError) as tpe:
        print(tpe)
    else:
        print("You are logged in")
        break
