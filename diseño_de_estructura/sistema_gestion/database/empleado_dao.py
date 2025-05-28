class EmpleadoDAO:
	def __init__(self, db_conn):
		self.conn = db_conn.get_connection()
		self.cursor = self.conn.cursor()
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                              (nombre TEXT, edad INTEGER, puesto TEXT)''')
		
	def agregar_empleado(self, empleado):
		self.cursor.execute("INSERT INTO empleado VALUES (?, ?, ?)",
                            empleado._nombre, empleado._edad, empleado._puesto)
		self.conn.commit()

	def mostrar_empleados(self):
		self.cursor.execute("SELECT * FROM empleados")
		for row in self.cursor.fetchall():
			print(row)