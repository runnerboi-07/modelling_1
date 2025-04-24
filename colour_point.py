from point import Point
import random

class ColourPoint(Point):
    def __init__(self, x, y, colour):
        """
        Initialises a ColourPoint object + Raises an exception if person tries to enter not a number
        :param x: x coordinate as an integer or float
        :param y: y coordinate as an integer or float
        :param colour: name of the colour as a string
        """
        if not isinstance(x, (int, float)): # x, tuple; isinstance asks what is the type of x
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y) # access parent class through super() (do not have to write self.x & self.y again); replaces self.x & self.y
        self.colour = colour # edit __init__ & everything else carries over from Point

    def __str__(self):
        """
        Dunder to show how the object will look when printed
        :return: print output
        """
        return f"<{self.colour}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColourPoint(1, 2, "red")

    print(p.distance_to_orig())
    print(p)
    # colours = ["red", "green", "blue", "yellow", "black", "magenta",
    #            "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # colour_points = []
    # for i in range(10):
    #     colour_points.append(
    #         ColourPoint(random.randint(-10, 10),
    #                     random.randint(-10, 10),
    #                     random.choice(colours)))
    #
    # print(colour_points)
    # colour_points.sort()
    # print(colour_points)