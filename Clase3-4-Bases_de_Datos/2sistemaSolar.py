import sqlite3

conexion = sqlite3.connect('Sistema Solar')

puntero = conexion.cursor()
##############################################
"""
puntero.execute("CREATE TABLE PLANETAS (NOMBRE VARCHAR(20), POSICION INTEGER, COLOR VARCHAR(10))")

variosPlanetas = [
	("Mercurio", 1, "Verde"),
	("Venus", 2, "Gris"),
	("Tierra", 3, "Azul")
]

puntero.executemany("INSERT INTO PLANETAS VALUES( ?, ?, ?)", variosPlanetas)
"""

puntero.execute("SELECT * FROM PLANETAS")

print(puntero.fetchall())

##############################################
conexion.commit()

conexion.close()