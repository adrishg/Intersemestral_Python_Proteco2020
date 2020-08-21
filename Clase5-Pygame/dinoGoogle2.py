#Importar el módulo pygame
import pygame
import time #Para poder usar el sleep

#Vamos a cargar las imágenes
spritesDino=[pygame.image.load('Sprites/d1.png'), pygame.image.load('Sprites/d2.png'), pygame.image.load('Sprites/d3.png'), pygame.image.load('Sprites/d4.png')]
fondo = pygame.image.load('Sprites/desierto.png')
cactus = pygame.image.load('Sprites/cactus.png')
imagenGameOver= pygame.image.load('Sprites/game_over.png')

#Inicializar pygame
pygame.init()

#Características de nuestra venta
altoVentana = 228 #todas las dimensiones en el código corresponden a píxeles
anchoVentana = 513

#Con ayuda de pygame creamos nuestra ventana
ventana = pygame.display.set_mode((anchoVentana, altoVentana))

#Título a nuestra ventana
pygame.display.set_caption("Mi juego de dinosaurio")

#Elemento reloj para tener una idea del tiempo
reloj = pygame.time.Clock()

#Posiciones de elemento cactus
anchoCactus= 25
altoCactus= 48
xCactus=325
yCactus=228-60


#Son las posiciones de nuestro rectángulo
x= 0
y= 228-53
#Las dimensiones de nuestro rectángulo
width = 44
height = 53

#cadaa vez que se presiona una tecla nuestro rectángulo cambia de posición en 5 píxeles
velocidad = 5

#Variables relacionadas a saltar
estaSaltando = False #Porque en principio no está saltando
contadorSalto= 10

#Variables relacionadas a caminar
contadorPasos = 0

#La variable run nos indica si el juego está corriendo
run = True
#Entra al while principal del juego que nos lleva a todo el flujo 
while run:
	#pygame.time.delay(50)
	reloj.tick(12)
	#Va capturando los acciones que hace el usuario con respecto a nuestra ventana
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			run = False
	#En la variable teclas tendremos que está presionando el usuario en su teclado
	teclas = pygame.key.get_pressed()
	#Cuando la tecla sea -> vamos a cambiar la posición en x
	#x>velocidad es un truco para que el elemento rectangulo no salga de la ventana
	if teclas[pygame.K_LEFT] and x>0: 
		x=x-velocidad
	#Tecla <- sumamos a la posición en x y verificamos que no se salga de la ventana
	if teclas[pygame.K_RIGHT] and x<(anchoVentana-width):
		x=x+velocidad
	#En caso de presionar la tecla espacio, esta saltando = True
	if teclas[pygame.K_SPACE]:
		estaSaltando = True
	if estaSaltando:
		if contadorSalto >=-10: #10>=-10 True entonces entra
			aux=1 #Declaramos auxiliar positivo
			if contadorSalto<0:
				aux=-1 #Auxiliar negativo---> todo lo que sube tiene que bajar
			#Cambiamos la posición de y, es una función cuadrática para ver cierta aceleración 
			y-= (contadorSalto **2)*.5*aux 
			contadorSalto-=1 #Contador empieza en 10 y se va restando hasta -10
		else: #Cuando el contador llega a -10 entra aquí, termino su salto y esta saltando e¿ahora es = False
			estaSaltando = False
			contadorSalto = 10 #Reinicamos el contado de nuevo en 10


	rectanguloDino = pygame.Rect(x,y, width, height)
	rectanguloCactus = pygame.Rect(xCactus, yCactus, anchoCactus, altoCactus)
	if rectanguloDino.colliderect(rectanguloCactus):
		ventana.blit(imagenGameOver, (50,50))
		pygame.display.flip()
		time.sleep(2)
		run=False


	ventana.blit(fondo, (0,0))
	#Se dibuja constantemente nuestro rectángulo (56, 184,141)-> corresponde a un azul turquesa
	#pygame.draw.rect(ventana, (56,184,141), (x,y, width, height))  
	if contadorPasos>=4:  ###Aquí estaba el error teníamos mayor a cuatro no menor o igual
	#Al usar el >= y elimando que el contador tenga la división entera ahora si iteramos sobre los 4 sprites y se mueven las patitas
		contadorPasos=0
	ventana.blit(cactus, (xCactus,yCactus))
	ventana.blit(spritesDino[contadorPasos],(x,y))
	contadorPasos=contadorPasos+1

	#Update nos ayuda a la fluidez del juego
	pygame.display.update()
#cerramos el init con un quit
pygame.quit()
