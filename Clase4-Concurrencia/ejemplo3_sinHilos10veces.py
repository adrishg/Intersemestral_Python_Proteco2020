import time

inicio = time.perf_counter()

def aDormir():
	print("Iniciando función, voy a dormir 1 s")
	time.sleep(1)
	print("Paso un segundo, he despertado")

#Ahora compararemos que pasa cuando ejecutamos 10 veces la función a
for _ in range(10):
	aDormir()

final = time.perf_counter()
print(f"Código ejecutado en {final- inicio, 2} segundos")