class Sensor:
    tipo: str = "Genérico"

    def __init__(self, sensor_id: str):
        self.id: str = sensor_id
        self.encendido: bool = False

    def activar(self):
        self.encendido = True
        print(f"Sensor {self.id} activado.")

    def desactivar(self):
        self.encendido = False
        print(f"Sensor {self.id} desactivado.")


class Camara(Sensor):
    tipo: str = "Cámara"

    def __init__(self, sensor_id: str, resolucion: str):
        Sensor.__init__(self, sensor_id)
        self.resolucion: str = resolucion


class SensorLuzLaser(Sensor):
    tipo: str = "Luz Laser"

    def __init__(self, sensor_id: str, alcance: int):
        Sensor.__init__(self, sensor_id)
        self.alcance: int = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo: str = "Vehículo Autónomo"

    def __init__(self, sensor_id: str, resolucion: str, alcance: int):
        Camara.__init__(self, sensor_id, resolucion)
        SensorLuzLaser.__init__(self, sensor_id, alcance)

    def mostrar_estado(self):
        print(f"--- {self.tipo} ---")
        print(f"ID: {self.id}")
        print(f"Resolución de Cámara: {self.resolucion}")
        print(f"Alcance de Láser: {self.alcance}m")
        print(f"Estado: {'Encendido' if self.encendido else 'Apagado'}")


if __name__ == "__main__":
    vehiculo = VehiculoAutonomo(sensor_id="VA-99", resolucion="4K", alcance=200)
    vehiculo.mostrar_estado()
    print()
    vehiculo.activar()
    vehiculo.mostrar_estado()