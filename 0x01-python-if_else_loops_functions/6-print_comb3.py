#!/usr/bin/python3
for m in range(9):
    for n in range(m + 1, 10):
        print("{}{}".format(m, n), end="\n" if m == 8 else ", ")
