import sys
import random


try:
    first_num = int(sys.argv[1])
    last_num = int(sys.argv[2])
    random_num = random.randint(first_num, last_num)

    print(f"Alright you pick number from {first_num} to {last_num}")
except ValueError:
    print("!!! Pleas Enter Number !!! RUN PROGRAM AGAIN !!!")
    sys.exit()


while True:
    try:
        user_num = int(input("Guess the number : "))

        if user_num < first_num or user_num > last_num:
            print("Pleas Enter Number in range")
        else:
            if user_num == random_num:
                print("You Win !")
                break
            else:
                print("Wrong ! try again")
    except ValueError:
        print("Pleas Enter Number Not STR")
