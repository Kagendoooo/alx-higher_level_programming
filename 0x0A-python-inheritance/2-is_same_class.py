#!/usr/bin/python3
"""Return True if the object is an instance of class ; otherwise False."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj: object to check.
        a_class: class to match the type of obj to.
    Returns:
        True / False.
    """
    if type(obj) == a_class:
        return True
    return False
