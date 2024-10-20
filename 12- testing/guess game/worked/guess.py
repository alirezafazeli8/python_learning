import random


# generate random number
def generate_number(num_one, num_two):
    return random.randint(num_one, num_two)


# store random number
answer = generate_number(1, 10)


def get_user_input():
    try:
        usr_input = int(input("Guess Number 1 - 10 : "))
        return usr_input
    except:
        pass


def user_input_error_handle(user_input):
    try:
        if 0 < user_input < 11:
            return user_input
        else:
            print("Pleas Enter Between 1 to 10")
    except TypeError:
        print("Pleas Enter Number")


def check_answer(system_answer):
    while True:
        user_input = user_input_error_handle(get_user_input())
        if system_answer == user_input:
            print("You Are Genius")
            break


if __name__ == "__main__":
    check_answer(answer)
