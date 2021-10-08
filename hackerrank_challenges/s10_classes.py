"""
DESAFIOS HACKERRANK
10. Classes
"""

# 1/2 Classes
'''import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real  #
        self.imaginary = imaginary  #
        
    def __add__(self, no):
        pass
    def __sub__(self, no):
        pass
    def __mul__(self, no):
        pass
    def __truediv__(self, no):
        pass
    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
# '''

# 2/2 Find the Torsional Angle (easy)
'''import math


class Points(object):  # ***** AINDA NAO ESTA CLARO PARA MIM *****
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z+other.z

    def cross(self, other):
        return Points(self.x*other.x, self.y*other.y, self.z*other.z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


# __main__
points = list()
for _ in range(4):
    a = list(map(float, input().split()))
    points.append(a)

a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
print(points)
x = (b - a).cross(c - b)
y = (c - b).cross(d - c)
angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

print("%.2f" % math.degrees(angle))  # '''