#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    try:
        for i in range(0, x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                element += 1
    except (ValueError, TypeError):
        pass
    print("")
    return element
