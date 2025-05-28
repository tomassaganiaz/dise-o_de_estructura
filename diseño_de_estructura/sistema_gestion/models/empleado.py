from models.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self._puesto = puesto

    def mostrar_info(self):
        print(f"Empleado: {self._nombre}, Edad: {self._edad}, Puesto: {self._puesto}")
