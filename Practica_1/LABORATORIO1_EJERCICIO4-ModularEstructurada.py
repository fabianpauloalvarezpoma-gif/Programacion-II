import math

def promedio(valores):
    suma = 0
    for numero in valores:
        suma = suma + numero
    n = len(valores)
    resultado = suma / n
    return resultado

def desviacion(valores):
    prom = promedio(valores)
    n = len(valores)

    suma_de_diferencias = 0
    for numero in valores:
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

    prom = promedio(valores)
    desv = desviacion(valores)

    print("El promedio es", round(prom, 2))
    print("La desviacion estandar es", round(desv, 5))


main()