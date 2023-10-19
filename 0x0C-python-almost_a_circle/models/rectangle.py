#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle
        Args:
            width: width of the new rectangle
            height: height of the new rectangle
            x: x coordinate of the new rectangle
            y: y coordinate of the new rectangle
            id: identity of the new rectangle
        Raises:
            TypeError: if either of width/height is not an integer
            ValueError: if either of width/height less than or equal 0
            TypeError: if either of x/y is not an integer
            ValueError: if either of x/y less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args: new attribute values.
                - 1st argument reps id attribute
                - 2nd argument reps width attribute
                - 3rd argument reps height attribute
                - 4th argument reps x attribute
                - 5th argument reps y attribute
            **kwargs (dict): value pairs of attributes
        """
        if args and len(args) != 0:
            i = 0
            for a in args:
                if i == 0:
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif k == "width":
                    self.width = j
                elif k == "height":
                    self.height = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """return the dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the print() and str() representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
