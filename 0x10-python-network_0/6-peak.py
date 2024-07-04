#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """find peak in a list """
    if not list_of_integers:
        return None

    i, j = 0, len(list_of_integers) - 1

    while i < j:
        mid = (i + j) // 2

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            j = mid
        else:
            i = mid + 1

    return list_of_integers[i]
