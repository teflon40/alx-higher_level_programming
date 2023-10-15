#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num_of_args = len(sys.argv) - 1
    if num_of_args == 0:
        print("{:d} arguments.".format(num_of_args))
    else:
        i = 1
        print("{:d} arguments:".format(num_of_args))
        while i <= num_of_args:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
