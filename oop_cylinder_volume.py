class Cylinder(object):

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.radius = radius
        self.height = height

    def volume(self):
     return (self.pi * self.radius ** 2 * self.height)

    def surface_area(self):
        return (2 * self.pi * self.radius * self.height) + (2 * self.pi * self.radius  ** 2)


x = Cylinder(2,3)

print x.volume()
print x.surface_area()


