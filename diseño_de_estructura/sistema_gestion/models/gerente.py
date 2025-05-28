from models.persona import Persona

class Gerente(Persona):
    def __init__(self, nombre, edad, departamento):
        super().__init__(nombre, edad)
        self._departamento = departamento

    def mostrar_info(self):
        print(f"Gerente: {self._nombre}, Edad: {self._edad}, Departamento: {self._departamento}")
