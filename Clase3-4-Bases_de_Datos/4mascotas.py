import sqlite3

conexion = sqlite3.connect("Tienda de mascotas")

puntero = conexion.cursor()
###########################################
"""
puntero.execute('''
	CREATE TABLE MASCOTA(
	ID_MASCOTA INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE VARCHAR(10),
	PESO INTEGER)
''')
"""
"""
puntero.execute('INSERT INTO MASCOTA VALUES(NULL, "Nanu", 11)')
"""
"""
variasMascotas = [
	("Rocco", 35),
	("Luna", 8)
]

puntero.executemany("INSERT INTO MASCOTA VALUES(NULL,?,?)", variasMascotas)
"""
"""
#READ
puntero.execute('SELECT * FROM MASCOTA WHERE PESO = 11')

seleccion = puntero.fetchall()

print(seleccion)
"""
"""
#UPDATE

puntero.execute('UPDATE MASCOTA SET NOMBRE = "Nanu" WHERE NOMBRE = "Nani"')
"""
"""
#DELETE
puntero.execute("DELETE FROM MASCOTA WHERE NOMBRE = 'Nanu'")
"""

###########################################
conexion.commit()

conexion.close()