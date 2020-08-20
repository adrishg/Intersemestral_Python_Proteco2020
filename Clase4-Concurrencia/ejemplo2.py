import time
import threading

inicio= time.perf_counter()

def aDormir():
	print("Inicializando ")
	time.sleep(1)
	print("Paso un segundo y ya desperté")

#Al código anterior le agregaremos manejo de hilos
#Creamos hilo 1 y 2 (con la función a dormir)
hilo1 = threading.Thread(target=aDormir)
hilo2 = threading.Thread(target=aDormir) 

#Y los inicializamos para que se empiecen a ejecutar
hilo1.start()
hilo2.start()

#Usamos join para que uno espere al otro en cuestión de ejecución antes de 
#continuar con el resto del código, recuerden que cuando omitimos join se 
#iba directo a imprimir el tiempo de ejecución sin que hubiera empezado hilo2
hilo1.join()
hilo2.join()


final = time.perf_counter()
print( f"Nuestro código se ejecute en {final-inicio} segundos")
#El tiempo de ejecución será alrededor de un segundo
