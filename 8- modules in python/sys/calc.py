import sys


def show_result(number_one, number_two, operator, result):
    print(f"{number_one} {operator} {number_two} = {result}")


if len(sys.argv) > 4:
    print("Usage Error !")
    sys.exit()
else:
    [file_name, number_one, operator, number_two] = sys.argv
    number_one = int(number_one)
    number_two = int(number_two)

    operating = {
        "+": lambda number_one, number_two: number_one + number_two,
        "-": lambda number_one, number_two: number_one - number_two,
        "*": lambda number_one, number_two: number_one * number_two,
        "/": lambda number_one, number_two: number_one / number_two,
    }

    try:
        show_result(
            number_one,
            number_two,
            operator,
            operating[operator](number_one, number_two),
        )
    except:
        print("Error! try again.")
