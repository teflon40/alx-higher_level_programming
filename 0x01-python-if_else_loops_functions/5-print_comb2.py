#!/usr/bin/python3

"""Prints numbers from 0 to 99"""
for num in range(0, 100):
    print("{:02d}{}".format(num, "\n" if num == 99 else ", "), end='')
