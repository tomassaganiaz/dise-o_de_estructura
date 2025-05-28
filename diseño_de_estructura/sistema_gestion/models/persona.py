from abc import ABC, abstractclassmethod

class Persona(ABC):
	def __init__(self, nombre, edad):
		self._nombre = nombre
		self._edad = edad

	@abstractclassmethod
	def mostrar_info(self):
		pass


