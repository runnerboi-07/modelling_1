from colour_point import ColourPoint

class AdvancedPoint(ColourPoint):
    COLOURS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"] # class attributes use capital letter - same for all classes
    def __init__(self, x, y, colour):
        if colour not in self.COLOURS:
            raise TypeError(f"Invalid colour, must be one of {self.COLOURS}")
        super().__init__(x, y, colour)
    # pass # no code needed here so pass; same as colour point

    @classmethod
    def add_colour(cls, colour): # cls is short for class; about whole class, not individual instance like in self
        """
        Adds a new valid colour for our class
        """
        cls. COLOURS.append(colour)

    @staticmethod # factory method since it defines a new instance
    def from_tuple(coordinate, colour = "red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, colour)

    @staticmethod # @ is a decorator
    def distance_2_points(p1, p2):
        return((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p): # self & p the other point
        return ((self.x - p.x) ** 2 + (self.y + p.y) ** 2) ** 0.5

AdvancedPoint.add_colour("rojo")
p = AdvancedPoint(1, 2, "rojo")
print(p)
print(p.distance_to_orig())
p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))