sistema_gestion/
│
├── main.py                          # Punto de entrada al sistema
│
├── models/                          # Clases relacionadas a lógica y estructura
│   ├── persona.py                   # Clase abstracta Persona
│   ├── empleado.py                  # Clase Empleado
│   ├── gerente.py                   # Clase Gerente
│
├── database/                        # Conexión y manejo de base de datos
│   ├── database_connection.py       # Singleton para la conexión
│   ├── empleado_dao.py              # Data Access Object para empleados
│
├── core/                            # Lógica principal del sistema
│   └── sistema_gestion.py           # Clase controladora con menú
│
├── db/                              # Carpeta opcional para la base de datos
│   └── empleados.db                 # Base de datos SQLite (autogenerada)
│
└── README.md                        # Documentación del proyecto
