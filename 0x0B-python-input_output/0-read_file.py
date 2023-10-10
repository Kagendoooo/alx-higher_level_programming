#!/usr/bin/python3
"""A test reading function"""


def read_file(filename=""):
    """print the contents of a UTF* txt file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
