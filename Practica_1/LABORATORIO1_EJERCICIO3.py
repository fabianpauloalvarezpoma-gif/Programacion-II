import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b + math.sqrt(discriminante)) / (2 * self.__a)

    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return 0
        return (-self.__b - math.sqrt(discriminante)) / (2 * self.__a)


def main():
    a, b, c = map(float, input("Ingrese a, b, c: ").split())

    ecuacion = EcuacionCuadratica(a, b, c)
    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        r1 = ecuacion.getRaiz1()
        r2 = ecuacion.getRaiz2()
        print(f"La ecuacion tiene dos raices {r1:.6g} y {r2:.6g}")
    elif discriminante == 0:
        r1 = ecuacion.getRaiz1()
        print(f"La ecuacion tiene una raiz {r1:.6g}")
    else:
        print("La ecuacion no tiene raices reales")

if __name__ == "__main__":
    main()
