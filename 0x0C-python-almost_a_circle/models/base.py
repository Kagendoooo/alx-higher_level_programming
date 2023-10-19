#!/usr/bin/python3

"""Defines a base model class."""


class Base:
    """rep base model
    Attributes:
    __nb_objects: number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id: identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
