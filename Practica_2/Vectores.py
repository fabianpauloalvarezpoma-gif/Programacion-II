import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            return Vector3D(self.x * otro, self.y * otro, self.z * otro)
        elif isinstance(otro, Vector3D):
            return (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        longitud = abs(self)
        if longitud == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / longitud, self.y / longitud, self.z / longitud)

    def producto_cruz(self, otro):
        cruz_x = (self.y * otro.z) - (self.z * otro.y)
        cruz_y = (self.z * otro.x) - (self.x * otro.z)
        cruz_z = (self.x * otro.y) - (self.y * otro.x)
        return Vector3D(cruz_x, cruz_y, cruz_z)


a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)

print(a + b)
print(a * 2)
print(round(abs(a), 4))
print(a.normal())
print(a * b)
print(a.producto_cruz(b))