#!/usr/bin/python3

import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
else:
    print("{:d} is {}".format(number, "negative" if number < 0 else "zero"))
