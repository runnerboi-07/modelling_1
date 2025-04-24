from colour_point import ColourPoint

class AdvancedPoint(ColourPoint):
    COLOURS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"] # class attributes use capital letter - same for all classes
    def __init__(self, x, y, colour):
        """
        Initialises AdvancedPoint object (similar to what we did for Point & ColourPoint; ColourPoint inherited here & obviously ColourPoint inherited Point previously)
        :param x: coordinate of x as an integer or float
        :param y: coordinate of y as an integer or float
        :param colour: colour as a string
        """
        if colour not in self.COLOURS:
            raise TypeError(f"Invalid colour, must be one of {self.COLOURS}")
        self._x = x # underscore (_x) convention used to signal private attributes that you would not want the user to alter
        self._y = y
        self._colour = colour
    # pass # no code needed here so pass; same as colour point

    @property # property decorator used to define getter methods
    def x(self): # can now use x instead of ._x to retrieve the attribute
        """
        Getter method defined to allow value of ._x attribute of the instance to be retrieved
        :return: value of self._x
        """
        return self._x # getter method

    @x.setter
    def x(self, value):
        """
        Setter method defined - allows property x to control setting of ._x
        :param value: new value for x set by user (could add if, else here to filter out unreasonable non int, float values)
        :return: none, value modified
        """
        self._x = value # "setter" method - you can set new value as per the rules we decide

    @property
    def y(self):
        """
        Getter method defined to allow value of ._y attribute of the instance to be retrieved
        :return: value of self._y
        """
        return self._y

    @property
    def colour(self):
        """
        Getter method defined to allow value of ._colour attribute of the instance to be retrieved
        :return: value of self._colour
        """
        return self._colour

    @classmethod # @ is a decorator
    def add_colour(cls, colour): # cls is short for class; about whole class, not individual instance like in self
        """
        Adds a new valid colour for our class
        :param colour: colour as a string
        :return: none, only list modified
        """
        cls.COLOURS.append(colour)

    @staticmethod # factory method since it defines a new instance; static method resides under namespace of class, but not really related to the class
    def from_tuple(coordinate, colour = "red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        :param coordinate: x and y values in tuple form
        :param colour: colour as a string, "red" set as default, but can be changed by user
        :return: newly created AdvancedPoint object
        """
        x, y = coordinate
        return AdvancedPoint(x, y, colour)

    @staticmethod
    def distance_2_points(p1, p2): # static method not bound to any specific instance here
        """
        Function to calculate distance between two chosen points p1 and p2
        :param p1: coordinates of p1
        :param p2: coordinates of p2
        :return: calculation result of distance
        """
        return((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p): # self & p the other point
        """
        Function to calculate distance between current instance of the object (self) and another point
        :param p: other point's coordinates
        :return: calculation result of distance
        """
        return ((self.x - p.x) ** 2 + (self.y + p.y) ** 2) ** 0.5

AdvancedPoint.add_colour("rojo") # uses class method to add new colour to class attribute "COLOURS"
p = AdvancedPoint(1, 2, "rojo")
p._x = 11
print(p)
print(p.distance_to_orig())
p2 = AdvancedPoint.from_tuple((3, 2)) # static method used to enter coordinates using tuple
print(p2)
print(AdvancedPoint.distance_2_points(p, p2)) # static method that takes points p & p2 as the parameters
print(p.distance_to_other(p2)) # regular method used here that takes first parameter as self