#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    num = 0
    for element in my_list[:x]:
        try:
            print(element, end='')
            num += 1
        except IndexError:
            pass
    return num
