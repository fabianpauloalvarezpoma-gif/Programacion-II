import math

class Estadistica:
    def __init__(self, valores):
        self.__valores = valores

    def promedio(self):
        suma = 0
        for numero in self.__valores:
            suma = suma + numero
        n = len(self.__valores)
        resultado = suma / n
        return resultado

    def desviacion(self):
        prom = self.promedio()
        n = len(self.__valores)

        suma_de_diferencias = 0
        for numero in self.__valores:
            diferencia = numero - prom
            suma_de_diferencias = suma_de_diferencias + (diferencia * diferencia)

        varianza = suma_de_diferencias / (n - 1)
        resultado = math.sqrt(varianza)
        return resultado

def main():
    print("Ingrese 10 numeros separados por espacio:")
    entrada = input()
    valores_texto = entrada.split()
    valores = []
    for texto in valores_texto:
        valores.append(float(texto))
    estadistica = Estadistica(valores)
    prom = estadistica.promedio()
    desv = estadistica.desviacion()
    print("El promedio es", round(prom, 2))
    print("La desviacion estandar es", round(desv, 5))
main()