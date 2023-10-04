#!/usr/bin/python3
for ch in range(122, 96, -1):
    print("{:c}".format(ch if ch % 2 == 0 else ch - 32), end="")
