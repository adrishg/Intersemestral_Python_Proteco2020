import time
import threading

inicio = time.perf_counter()

def aDormir():
	print("Iniciando función, voy a dormir 1 s")
	time.sleep(1)
	print("Paso un segundo, he despertado")

#Vamos a comparar ahora creando dos hilos
#Para luego poder iterar sobre todos los hilos crearemos una lista vacia llamada hilos
hilos=[]
#En un bucle fos crearemos 10 hilos
for _ in range(10):
	hilo = threading.Thread(target= aDormir)
	hilo.start()
	#Y guardaremos todos los hilos creados en nuestra lista hilos
	hilos.append(hilo)

#Ahora iterando en hilos vamos a unirlos para que esperen a la ejecución de todos antes 
#de continuar con el código siguiente, en este caso la impresión del tiempo de ejecución
for h in hilos:
	h.join()


aDormir()

final = time.perf_counter()
print(f"Código ejecutado en {final- inicio, 2} segundos")