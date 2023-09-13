#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum({i for i in my_list if isinstance(i, int)})
