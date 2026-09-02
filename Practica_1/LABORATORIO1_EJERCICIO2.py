class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def __determinante(self):
        return (self.__a * self.__d) - (self.__b * self.__c)

    def tieneSolucion(self):
        return self.__determinante() != 0

    def getX(self):
        det = self.__determinante()
        return ((self.__e * self.__d) - (self.__b * self.__f)) / det

    def getY(self):
        det = self.__determinante()
        return ((self.__a * self.__f) - (self.__e * self.__c)) / det

a, b, c, d, e, f = map(float, input("Ingrese los datos de: a, b, c, d, e, f: ").split())
ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")