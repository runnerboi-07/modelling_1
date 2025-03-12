from point import Point
import random

class ColourPoint(Point):
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour # edit __init__ & everything else carries over from Point

    def __str__(self):
        return f"<{self.colour}: {self.x}, {self.y}>"

p = ColourPoint(1, 2, "red")
print(p)
colours = ["red", "green", "blue", "yellow", "black", "magenta",
           "cyan", "white", "burgundy", "periwinkle", "marsala"]
colour_points = []
for i in range(10):
    colour_points.append(
        ColourPoint(random.randint(-10, 10),
                    random.randint(-10, 10),
                    random.choice(colours)))

print(colour_points)
colour_points.sort()
print(colour_points)