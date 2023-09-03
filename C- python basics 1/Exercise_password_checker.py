# input username
username = input("Pleas Enter Your UserName : ")

# input password
password = input("Pleas Enter Your Password : ")

# get password length
password_len = "*" * len(password)

# print password and password length
show_password = f"{username} Password is : {password_len} and {len(password)} long."

print(show_password)
