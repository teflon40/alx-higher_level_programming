#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{:d} arguments.".format(num_args))
    else:
        arg_str = "argument" if num_args == 1 else "arguments"
        i = 1
        print("{:d} {:s}:".format(num_args, arg_str))
        while i <= num_args:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
