#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import div, add, sub, mul

    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    op = argv[2]
    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    if op == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
