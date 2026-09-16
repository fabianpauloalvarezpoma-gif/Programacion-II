import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, a, b=None):
        if b == None:
            otro_punto = a
            d_x = otro_punto.get_x() - self.x
            d_y = otro_punto.get_y() - self.y
        else:
            d_x = a - self.x
            d_y = b - self.y

        return math.sqrt(d_x**2 + d_y**2)


p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1:",     p1.get_x(), ",", p1.get_y())
print("Punto 2:",     p2.get_x(), ",", p2.get_y())

resultado1 = p1.distancia(p2)
print("Distancia enviando un objeto:", resultado1)

resultado2 = p1.distancia(10, 30.5)
print("Distancia enviando coordenadas:", resultado2)