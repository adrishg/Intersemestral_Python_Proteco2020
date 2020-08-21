import sqlite3

conexion = sqlite3.connect("PROTECO")

puntero = conexion.cursor()

##############################################
"""
puntero.execute('''
	CREATE TABLE ESTUDIANTE (
	ID_ESTUDIANTE VARCHAR(5) PRIMARY KEY NOT NULL,
	NOMBRE VARCHAR(10) UNIQUE,
	CURSO VARCHAR(20),
	CALIFICACION INTEGER)
''')
"""
"""
variosEstudiantes = [
	("qwer1", "Luis Velasco", "Machine Learning I", 10),
	("123nm", "Luis Rosas", "Python Básico", 9),
	("qwer2", "Ana Sánchez", "Python Intermedio", 8)
]

puntero.executemany("INSERT INTO ESTUDIANTE VALUES(?,?,?,?)", variosEstudiantes)

"""

puntero.execute("INSERT INTO ESTUDIANTE VALUES('QWER2','Mario Vásquez', 'Python Básico', 9)")

##############################################

conexion.commit()

conexion.close()