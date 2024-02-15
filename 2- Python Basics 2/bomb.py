# import random library
import random

# numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# computer random choice list numbers
computer_choice = random.choice(numbers)

# user try counter
user_try = 5

while True:

    # user input choice
    user_input = int(input("Guess Number between 1 and 10 :"))
    
    if user_input == computer_choice:
        print('God damn right choice 💣')
        break
    elif user_try == 0:
        print("You Died 🥹")
        break
    elif user_input > computer_choice:
        print(f'number is greater , chose less than. {user_try} time remain')
        user_try -= 1
    elif user_input < computer_choice:
        print(f'number is less , chose greater than. {user_try} time remain')
        user_try -= 1