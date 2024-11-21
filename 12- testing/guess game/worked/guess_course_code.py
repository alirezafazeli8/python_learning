import random


def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print("You Win !")
                return True
        else:
            print("Enter Number Between 1 and 10")
            return False
    except:
        return False


answer = random.randint(1, 10)


if __name__ == "__main__":
    while True:
        try:
            guess = int(input("Enter Number : "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Pleas Enter Number !!!!")
            continue
