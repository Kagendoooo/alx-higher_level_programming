#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    res = add(a, b)
    print("{} + {} = {}".format(a, b, res))

    res = sub(a, b)
    print("{} - {} = {}".format(a, b, res))

    res = mul(a, b)
    print("{} * {} = {}".format(a, b, res))

    res = div(a, b)
    print("{} / {} = {}".format(a, b, res))
