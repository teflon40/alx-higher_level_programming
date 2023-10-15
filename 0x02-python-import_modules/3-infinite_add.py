#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num = len(sys.argv) - 1
    sum = 0
    i = 1
    while i <= num:
        sum += int(sys.argv[i])
        i += 1
    print("{:d}".format(sum))
