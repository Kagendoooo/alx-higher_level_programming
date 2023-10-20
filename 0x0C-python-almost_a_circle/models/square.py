#!/usr/bin/python3

"""defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size: size of the new square
            x: x coordinate of the new square
            y: y coordinate of the new square
            id: identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square
        Args:
            *args: new attribute values.
            - 1st argument reps id attribute
            - 2nd argument reps size attribute
            - 3rd argument reps x attribute
            - 4th argument reps y attribute
        **kwargs: New value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif k == "size":
                    self.size = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """return the dictionary reps of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the print() and str() rep of a square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
