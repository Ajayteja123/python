class Circle:
    pi = 3.14  # class virable

    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        area = Circle.pi*self.radius*self.radius  # delcaring class viarble
        return area


c = Circle(4)
print(c.area_of_circle())
