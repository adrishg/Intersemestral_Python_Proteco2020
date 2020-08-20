#Importamos el módulo time
import time

#Creamos una variable que guardará el momento en el que empiece la ejecución
inicio = time.perf_counter()

#Creamos una función que duerme 1s
def aDormir():
	print("Inicializando ")
	time.sleep(1)
	print("Paso un segundo y ya desperté")

#Mandamos a llamar dos veces la función a dormir
aDormir()
aDormir()

#Creamos una variable que nos diga cuando acabo la función
final = time.perf_counter()
#Restamos el final menos el inicio para saber cuantos s tardó nuesta ejecución
print( f"Nuestro código se ejecute en {final-inicio} segundos")
#Ya que durmió 1 s cada vez tendremos una ejecución aproximada de 2.0001 segundos