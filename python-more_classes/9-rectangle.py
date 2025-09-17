#!/usr/bin/python3
""" Defines an empty Rectangle class. """


class Rectangle:
    """Represents a rectangle."""

    # pulic class attribute
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Class Rectangle.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        # increment when instance created
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    # ----- width -----
    @property
    def width(self):
        """ Get the width of Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of Rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    # ----- height -----
    @property
    def height(self):
        """ Get the height of Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of Rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    # ----- Public methods -----
    def area(self):
        """Return the area of the Rectangle."""
        # self.height is better than self.__height
        # this will get from getter - property
        return (self.height * self.width)
        print

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    # ----- string forms -----
    def __str__(self):
        """
        Return the rectangle drawn with '#' characters.
        Empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ("")
        rect_str = ""
        # height = row, width = how many # in each row
        for h in range(self.height):
            # use str() to ensure print_symbol is string
            rect_str = rect_str + str(self.print_symbol) * self.width
            if h != self.height - 1:  # start new line if it's not last
                rect_str = rect_str + "\n"
        return rect_str

    def __repr__(self):
        """ Return a string that can recreate the object. """
        # Rectangle(width, height)
        return f"Rectangle({self.width}, {self.height})"

    # ----- delete method -----
    def __del__(self):
        """Called when an instance is deleted."""
        print("Bye rectangle...")
        # decrement when deleted
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    # ----- static method -----
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.

        Args:
            rect_1: 1st rect
            rect_2: 2nd rect
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        # campare the rect_1.area()! not rect_1 itself!
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # ----- class method -----
    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle with width == height == size.

        Args:
            cls: class itself - Rectangle.
            size: the length of rectangle.
        """
        # Rectangle.square(5)
        # size = 5
        return cls(size, size)
