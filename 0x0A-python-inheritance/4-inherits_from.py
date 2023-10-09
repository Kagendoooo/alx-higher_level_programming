#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: object to check.
        a_class: class to match the type of obj to.
    Returns:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
