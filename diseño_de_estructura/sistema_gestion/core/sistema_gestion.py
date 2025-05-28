from database.database_connection import DatabaseConnection
from database.empleado_dao import EmpleadoDAO
from models.empleado import Empleado

class SistemaGestion:
    def __init__(self):
        self.db = DatabaseConnection()
        self.dao = EmpleadoDAO(self.db)

    def menu(self):
        while True:
            print("\n--- Menú del Sistema de Gestión ---")
            print("1. Agregar Empleado")
            print("2. Mostrar Empleados")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                puesto = input("Puesto: ")
                empleado = Empleado(nombre, edad, puesto)
                self.dao.agregar_empleado(empleado)
            elif opcion == "2":
                self.dao.mostrar_empleados()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
