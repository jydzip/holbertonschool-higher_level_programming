#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    fn = None

    if op == "+":
        fn = add
    elif op == "-":
        fn = sub
    elif op == "*":
        fn = mul
    elif op == "/":
        fn = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = fn(a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
