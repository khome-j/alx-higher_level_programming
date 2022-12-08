#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

args_len = len(sys.argv)


if args_len != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif sys.argv[2] not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

if sys.argv[2] == "+":
    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
elif sys.argv[2] == "-":
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
elif sys.argv[2] == "*":
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
else:
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
