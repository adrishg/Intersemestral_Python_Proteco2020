
print("CALCULADORA DE DIVISIONES\n")

try:
	num1=float(input("Ingresa el numerador:"))
	num2=float(input("Ingresa el denominador:"))
	resultado=(num1/num2)
	print("El resultado es:",resultado)

except TypeError:
	print("La division solo se puede hacer entre numeros")

except ZeroDivisionError:
	print("No puedes hacer divisones entre cero :(")

except ValueError:
	print("Debes ingresar unicamente numeros")

print("FIN DEL PROGRAMA")





def division(a,b):

	try:
		return(a/b)

	except ZeroDivisionError:
		print("No puedes dividir entre cero")

while True:
	try:
		num1=float(input("Ingresa el numerador:"))
		num2=float(input("Ingresa el denominador:"))

		print(division(num1,num2))
		break

	except  ValueError:
		print("DEBES INGRESAR UN NUMERO!!!!!!")







edad=17

if edad<18:
	raise Exception("Solo mayores de edad")




def sementre(no_semestre):
	
	if no_semestre<=0:
		raise ValueError("No puedes ingresar un numero negativo")
	elif no_semestre <=2:
		return ("Eres un bebe")
	elif no_semestre<=5:
		return ("Eres joven")
	elif no_semestre<10:
		return("Ya estas viejito")

try:
	print(sementre("w"))

except ValueError as Error_Num_Semestre:

	print(Error_Num_Semestre)

except TypeError:

	print("Solo ingresa numeros")

except NameError:

	print("Argumento invalido")

else: 

	print("El codigo ya te dijo que eres")

finally:

	print("Seguimos con la clase")



try:
	a=4/0
except Exception as e:
	print(e)
else:
	print("Se hizo la division")
finally:
	print("Gracias por usar la calculadora")


###PRUEBA 5

#	Explicar que except engloba todo los errores existentes
#	No es buena practica

try:
	numero=float(input("Ingresa un numero:"))

except Exception:
	print("Algo no esta bien")







try:
	num1=float(input("Ingresa el numero 1:"))
	num2=float(input("Ingresa el numero 2:"))

	print("Resultado es: ",num1**num2)

except ArithmeticError:
	print("SE PRODUJO EN ERROR MATEMATICO\n")

	try:
		print("Resultado es: ",num1**num2)

	except ZeroDivisionError:
		print("Division entre cero")

	except OverflowError:
		print("La operacion arroja un dato muuuuuuy grande")

	except Exception:
		print("New Error")




###PRUEBA
class ErrorPropio(Exception):

	def __init__(self,num1,num2):
		self.deudas=num1
		self.dinero=num2
	def resultado(self):
		return(self.dinero-self.deudas)

dinero=1000
deudas=100

try:
	if deudas>dinero:
		raise ErrorPropio(deudas,dinero)
	else:
		print("Puedes comprar")

except ErrorPropio as alias:
	print("No puede comprar, tiene una deuda de:",(alias.resultado()))


class ClaveBancaria(Exception):
    def __init__(self, clave1, clave2):
        self.clave1 = clave1
        self.clave2 = clave2

nip="holamundo"

try:
	intento=input("Ingresa tu contrasenia:")

	if intento==nip:

		print("BIENVENIDO")

	else:

		raise ClaveBancaria(nip,intento)

except ClaveBancaria as e:

    p1, p2 = e.args
    print("\t\tCUENTA BLOQUEDA\t\t\n")
    print("Ingresaste:",p2,"y la clave era:",p1)



###PRUEBA 6


try:
	f=open("file.txt","r")

except Exception as e:
	print("Error de archivo")