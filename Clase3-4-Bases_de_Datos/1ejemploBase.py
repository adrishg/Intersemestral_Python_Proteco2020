import sqlite3

conexion = sqlite3.connect("Base de datos")

puntero = conexion.cursor()

##############################################
"""
puntero.execute("CREATE TABLE MARAVILLAS (NOMBRE VARCHAR(30), ANTIGUEDAD INTEGER, PAIS VARCHAR(20))")
"""
puntero.execute("INSERT INTO MARAVILLAS VALUES(NULL, 1000)")
##############################################

conexion.commit()

conexion.close()