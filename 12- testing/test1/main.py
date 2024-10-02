def do_stuff(num):
    if isinstance(num, int) and num >= 1:
        return num**2
    else:
        return "use real number"


def do_stuff_2(num):
    return num + 2
