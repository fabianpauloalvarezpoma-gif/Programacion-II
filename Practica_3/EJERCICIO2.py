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

    def validaNumero(self, n: int, mostrar_error: bool = True) -> bool:
        return 0 <= n <= 10

    def juega(self):
        self.reiniciaPartida()
        while True:
            self.numeroAAdivinar = random.randint(0, 10)
            if self.validaNumero(self.numeroAAdivinar, mostrar_error=False):
                break

        print("\n--- Iniciando Partida ---")
        jugando = True
        while jugando:
            intento = int(input("Ingresa un número: "))
            if not self.validaNumero(intento, mostrar_error=True):
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                jugando = False
            else:
                quedan_vidas = self.quitaVida()
                if quedan_vidas:
                    if intento < self.numeroAAdivinar:
                        print("El número a adivinar es mayor.")
                    else:
                        print("El número a adivinar es menor.")
                    print(f"Vidas restantes: {self.vidasRestantes}")
                else:
                    print(f"Te quedaste sin vidas. El número era: {self.numeroAAdivinar}")
                    jugando = False


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)

    def validaNumero(self, n: int, mostrar_error: bool = True) -> bool:
        if 0 <= n <= 10 and n % 2 == 0:
            return True
        else:
            if mostrar_error:
                print("Error: El número debe ser par y estar entre 0 y 10.")
            return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)

    def validaNumero(self, n: int, mostrar_error: bool = True) -> bool:
        if 0 <= n <= 10 and n % 2 != 0:
            return True
        else:
            if mostrar_error:
                print("Error: El número debe ser impar y estar entre 0 y 10.")
            return False


if __name__ == "__main__":
    print("=== JUEGO ADIVINA NÚMERO DEL 0 AL 10 ===")
    j1 = JuegoAdivinaNumero(3)
    j1.juega()

    print("\n=== JUEGO ADIVINA NÚMERO PAR DEL 0 AL 10 ===")
    j2 = JuegoAdivinaPar(3)
    j2.juega()

    print("\n=== JUEGO ADIVINA NÚMERO IMPAR DEL 0 AL 10 ===")
    j3 = JuegoAdivinaImpar(3)
    j3.juega()