import math
class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def magnitud(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def sumar(self, b):
        x = self.__x + b.getX()
        y = self.__y + b.getY()
        z = self.__z + b.getZ()
        return AlgebraVectorial(x, y, z)

    def restar(self, b):
        x = self.__x - b.getX()
        y = self.__y - b.getY()
        z = self.__z - b.getZ()
        return AlgebraVectorial(x, y, z)

    def multiplicar(self, r):
        x = self.__x * r
        y = self.__y * r
        z = self.__z * r
        return AlgebraVectorial(x, y, z)

    def productoEscalar(self, b):
        return (self.__x * b.getX() + self.__y * b.getY() + self.__z * b.getZ())

    def productoVectorial(self, b):
        x = self.__y * b.getZ() - self.__z * b.getY()
        y = self.__z * b.getX() - self.__x * b.getZ()
        z = self.__x * b.getY() - self.__y * b.getX()

        return AlgebraVectorial(x, y, z)

    def perpendicular1(self, b):
        suma = self.sumar(b)
        resta = self.restar(b)
        return suma.magnitud() == resta.magnitud()

    def perpendicular2(self, b):
        ab = self.restar(b)
        ba = b.restar(self)
        return ab.magnitud() == ba.magnitud()

    def perpendicular3(self, b):
        return self.productoEscalar(b) == 0

    def perpendicular4(self, b):
        suma = self.sumar(b)
        return suma.magnitud()**2 == self.magnitud()**2 + b.magnitud()**2

    def paralela1(self, b, r):
        rb = b.multiplicar(r)

        return (self.__x == rb.getX() and
                self.__y == rb.getY() and
                self.__z == rb.getZ())

    def paralela2(self, b):
        producto = self.productoVectorial(b)

        return (producto.getX() == 0 and producto.getY() == 0 and producto.getZ() == 0)

    def proyeccion(self, b):
        producto = self.productoEscalar(b)
        modulo = b.magnitud()**2
        r = producto / modulo
        return b.multiplicar(r)

    def componente(self, b):
        producto = self.productoEscalar(b)
        modulo = b.magnitud()
        return producto / modulo

    def __str__(self):
        return "(" + str(float(self.__x)) + ", " + \
                    str(float(self.__y)) + ", " + \
                    str(float(self.__z)) + ")"

v1 = AlgebraVectorial(1, 0, 0)
v2 = AlgebraVectorial(0, 1, 0)
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Son perpendiculares?:", v1.perpendicular3(v2))
print("Son paralelos?:", v1.paralela2(v2))
print("Proyección de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en v2:", v1.componente(v2))