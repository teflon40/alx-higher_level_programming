#!/usr/bin/python3

# print ASCII alphabet in lowercase except 'q' and 'e'
for alpha in range(97, 123):
    print("{}".format(chr(alpha) if chr(alpha) not in "qe" else ""), end="")
