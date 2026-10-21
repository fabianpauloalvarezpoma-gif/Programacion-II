import random
class Juego:
    def __init__(self, numero_de_vidas: int):
        self.numeroDeVidas = numero_de_vidas
        self.vidasRestantes = numero_de_vidas
        self.record = 0

    def reiniciaPartida(self):
        self.vidasRestantes = self.numeroDeVidas

    def actualizaRecord(self):
        if self.vidasRestantes > self.record:
            self.record = self.vidasRestantes
            print(f"¡Nuevo récord alcanzado! Vidas restantes: {self.record}")

    def quitaVida(self) -> bool:
        self.vidasRestantes -= 1
        return self.vidasRestantes > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("=== Adivina el Número (0 a 10) ===")
        jugando = True
        while jugando:
            intento = int(input("Ingresa un número entre 0 y 10: "))
            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                jugando = False
            else:
                quedan_vidas = self.quitaVida()
                if quedan_vidas:
                    if intento < self.numeroAAdivinar:
                        print("El número a adivinar es mayor. Inténtalo de nuevo.")
                    else:
                        print("El número a adivinar es menor. Inténtalo de nuevo.")
                    print(f"Vidas restantes: {self.vidasRestantes}")
                else:
                    print(f"Ya no te quedan más vidas. El número era: {self.numeroAAdivinar}")
                    jugando = False

if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()