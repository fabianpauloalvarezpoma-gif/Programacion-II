import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return 0
        return (self.__finaliza - self.__inicia) * 1000

def ordenacion_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def main():
    cantidad = 100000
    numeros = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    cronometro = Cronometro()
    cronometro.inicia()
    print("Ordenando (esto puede tardar un rato con seleccion)")
    ordenacion_por_seleccion(numeros)
    cronometro.detener()
    print(f"Tiempo transcurrido: {cronometro.lapsoDeTiempo():.2f} ms")
    print(f"Tiempo transcurrido: {cronometro.lapsoDeTiempo() / 1000:.2f} s")
if __name__ == "__main__":
    main()

