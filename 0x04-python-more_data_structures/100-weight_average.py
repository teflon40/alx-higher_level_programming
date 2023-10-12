#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average"""
    if my_list == []:
        return 0
    avg_list = []
    weight = 0
    for integers in my_list:
        weight += integers[1]
        avg_list.append(integers[0] * integers[1])
    return sum(avg_list) / weight
