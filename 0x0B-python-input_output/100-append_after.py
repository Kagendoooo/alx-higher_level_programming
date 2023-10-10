#!/usr/bin/python3


"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert txt after each line containing a given string in a file
    Args:
        filename: name of the file
        search_string: string to search for within the file.
        new_string: string to insert
    """
    text = ""
    with open(filename) as i:
        for line in i:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
