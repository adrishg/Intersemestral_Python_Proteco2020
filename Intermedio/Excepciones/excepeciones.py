#import getpass

"""
print("CALCULADORA DE DIVISIONES\n")

try:
	num1=float(input("Ingrese el numerador:"))
	num2=float(input("Ingresa el denominador:"))

	resultado=num1/num2

	print("El resultado de la division:",resultado)

except TypeError:
	print("No puedo dividir cadenas")

except ZeroDivisionError:
	print("No puedes dividir entre cero")

except ValueError:
	print("Solo ingresa numeros")

print("Programa Terminado")





def division(a,b):
	try:
		return(a/b)

	except ZeroDivisionError:
		print("No puede entre cero")


while True:

	try:
		num1=float(input("Ingrese el numerador:"))
		num2=float(input("Ingresa el denominador:"))

		print(division(num1,num2))
		break

	except ValueError:
		print("Solo ingresa numeros")





edad=17

if edad<18:
	raise TypeError("Solo mayores de edad")





def semestre(no_semestre):

	if no_semestre<=0:
		raise ValueError("No puedes estar en un semestre negativo o semestre cero")

	elif no_semestre<=2:
		print("Eres un bb")

	elif no_semestre<=5:
		print("Ya eres un jovencito")

	elif no_semestre<10:
		print("Ya estas grandesito")

try:
	semestre(p)

except ValueError:
	print("Hubo un error")

else:
	print("El codigo ya te dijo que eres<3")

finally:
	print("Gracias por usar el codigo")

print("Continua....")


try:
	num1=float(input("Ingresa el primer numero:"))
	num2=float(input("Ingresa el segundo numero:"))

	print("El resultado es:",num1**num2)

except ArithmeticError:
	print("SE PRODUJO UN ERROR MATEMATICO")

	try:
		print("El resultado es:",num1**num2)

	except ZeroDivisionError:
		print("Estas diviendo entre cero")

	except OverflowError:
		print("La operacion arroja un numero muuuuuy grande")








class ClaveBancaria(Exception):
	def __init__(self,clave1,clave2):
		self.clave1=clave1
		self.clave2=clave2

nip="1010"

try:
	#Se utiliza el metodo getpass para no hacer visible la contraseña al escribir DEBEN IMPORTAR getpass
	#Agregar el inicio de nuestro progrma "import getpass" para hacer uso
	intento=getpass.getpass("Ingresa tu contrasenia:")

	if intento==nip:

		print("\t\tBIENVENIDO")

	else:

		raise ClaveBancaria(nip,intento)

except ClaveBancaria as hola:

	clave1,clave2=hola.args

	print("CUENTA BLOQUEADA")
	print("Ingresaste:",clave2," y la contrasenia era:",clave1)

class ErrorPropio(Exception):

	def __init__(self,num1,num2):
		self.deudas=num1
		self.dinero=num2

	def resultado(self):
		return(self.dinero-self.deudas)


deudas=20000
dinero=1000000

try:
	if deudas>dinero:
		raise ErrorPropio(deudas,dinero)

	else:
		print("Puedes comprar")

except ErrorPropio as alias:
	print("No puede comprar, tiene una deuda de:",abs(alias.resultado()))



"""