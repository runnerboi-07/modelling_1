import random

class Point:
    def __init__(self, x, y): # defines instance of 'Point'; automatically called
        # self = instance of point that we are instantiating
        # init is a magic method/dunder
        """
        Initialise a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x # define x attribute via self.x
        self.y = y # & assign the value of x to it

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):
        return self.__str__() # use same way of printing as str

    def distance_to_orig(self):
        return (self.x**2 + self.y**2)**0.5 # distance formula; square root of the sum of x & y squared

    def __gt__(self, other): # comparing self w/ other point
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance == other_distance

if __name__ == "__main__": # only run when this is the main file
    # Now we need to instantiate it:
    p = Point(1, 2) # p is an instance of 1 & 2
    p2 = Point(2, 3)
    p4 = Point(1, -55)
    print(f"p.x={p.x} & p.y={p.y}")
    print(f"p4.x={p.x} & p4.y={p.y}")

    p.x = 20 # can access & change attributes of the instance
    print(f"p.x={p.x} & p.y={p.y}")

    print(p) # First attempt: <__main__.Point object at 0x000002E22E797CB0> - does not know how to print since we have not assigned - gives location of point
    # we can create a custom print for our class

    # create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value
    print("I got these 5 random points:")
    for p in points:
        print(p)
    print(points) # printing container does not use __str__; need __repr__ (short for representation)

    # the final purpose is to sort the list of random points
    # points.sort() # .sort() does not know how to compare values in the list entered using Point
    # print(points)
    # 3 and 4 are Pythagorean numbers (3**2 + 4**2 = 5**2)
    p = Point(3, 4)
    print(p.distance_to_orig())
    p2 = Point(1, 1)
    print(f"I am checking p > p2: {p > p2}") # I expect to have True - __gt__ is working
    # can use break point to see how it works
    print(f"I am checking p == p2: {p == p2}")

    print(f"The sorted list of points is:")
    points.sort() # now the sort works after defining __gt__ & __eq__ to compare
    print(points)