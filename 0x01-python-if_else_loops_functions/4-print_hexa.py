#!/usr/bin/python3

"Prints all number from 0 to 98 in decimal and hexadecimal"
for number in range(0, 99):
    print("{:d} = 0x{:x}".format(number, number))
