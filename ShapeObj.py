from math import pi, sqrt

class Shape:
    
    count = 0 

    def __init__(self):
        Shape.count += 1
        self.id = Shape.count

    def print(self):
        print(f"{self.id}: {self.__class__.__name__}, perimeter: {self.perimeter()}, area: {self.area()}")

    def perimeter(self):
        return None

    def area(self):
        return None

    def getInfo(self):
        return f"{self.__class__.__name__}"

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.__class__.__name__ == other.__class__.__name__
        else:
            return False

    def __hash__(self):
        return hash(self.__class__.__name__)

    def resetCount():
        Shape.count = 0


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius

    # override
    def perimeter(self):
        return 2 * pi * self.radius
    
    def area(self):
        return pi * self.radius ** 2

    def print(self):
        print(f"{self.id}: {self.__class__.__name__}, perimeter: {self.perimeter():.5f}, area: {self.area():.5f}")

    def getInfo(self):
        return f"{self.__class__.__name__} {self.radius}"

    def __eq__(self, other):
        if isinstance(other, Shape):
            if self.__class__.__name__ == other.__class__.__name__:
                return self.radius == other.radius
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(self.__class__.__name__)


class Ellipse(Shape):
    def __init__(self, a, b):
        Shape.__init__(self)
        self.semiMajor = max(a,b)
        self.semiMinor = min(a,b)
        self.semiMa = a
        self.semiMi = b

    def area(self):
        return pi * self.semiMajor * self.semiMinor

    def eccentricity(self):
        try:
            return sqrt(self.semiMajor ** 2 - self.semiMinor ** 2)
        except:
            return None

    def print(self):
        print(f"{self.id}: {self.__class__.__name__}, perimeter: {self.perimeter()}, area: {self.area():.5f}, linear eccentricity: {self.eccentricity():.5f}")

    def getInfo(self):
        return f"{self.__class__.__name__} {self.semiMa} {self.semiMi}"

    def __eq__(self, other):
        if isinstance(other, Shape):
            if self.__class__.__name__ == other.__class__.__name__:
                return self.semiMajor == other.semiMajor and self.semiMinor == other.semiMinor
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(self.__class__.__name__)


class Rhombus(Shape):
    def __init__(self, diag1 , diag2):
        Shape.__init__(self)
        self.diagonal1 = diag1
        self.diagonal2 = diag2

    def perimeter(self):
        return 2 * sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2)
    
    def area (self):
        return (self.diagonal1 * self.diagonal2)/2

    def side(self):
        return sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2)/2

    def inradius(self):
        try:
            return (self.diagonal1 * self.diagonal2)/(2 * sqrt(self.diagonal1 ** 2 + self.diagonal2 ** 2))
        except:
            return None

    def print(self):
        print(f"{self.id}: {self.__class__.__name__}, perimeter: {self.perimeter():.5f}, area: {self.area():.5f}, side: {self.side():.5f}, in-radius: {self.inradius():.5f}")

    def getInfo(self):
        return f"{self.__class__.__name__} {self.diagonal1} {self.diagonal2}"

    def __eq__(self, other):
        if isinstance(other, Shape):
            if self.__class__.__name__ == other.__class__.__name__:
                return self.diagonal1 == other.diagonal1 and self.diagonal2 == other.diagonal2
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(self.__class__.__name__)