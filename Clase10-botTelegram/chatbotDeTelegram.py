from telegram.ext import Updater
import time

#Usen su taken de telegram:
updater = Updater(token="AQUÍ EL TOKEN", use_context=True)

dispatcher = updater.dispatcher

def saludar(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido al chatbot de Adriana")

def arremedar(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def hora(update, context):
	mensaje= 'La hora actual es:'+time.strftime("%X")
	context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)

##############################################################################3
from quote import quote
def frase(update, context):
	nombreDelAutor= ' '.join(context.args)
	resultado = quote(nombreDelAutor, limit=1)
	#El modulo quote cuando hace una busqueda por autor nos regresa un diccionario dentro de una lista
	frase= resultado[0]['quote']+"\n-"+resultado[0]['author']

	context.bot.send_message(chat_id=update.effective_chat.id, text=frase)
#Mimportar manejador de comandos
from telegram.ext import CommandHandler


manejadorFrase = CommandHandler('frase',frase)
dispatcher.add_handler(manejadorFrase)

###############################################################################3

manejadorSaludo = CommandHandler('start', saludar)
dispatcher.add_handler(manejadorSaludo)

#Importar un manejador pero ahora de mensajes y filtros
from telegram.ext import MessageHandler, Filters
manejadorArremedos= MessageHandler(Filters.text & (~Filters.command),arremedar)
dispatcher.add_handler(manejadorArremedos)

#Manejador de la función hola
manejadorHora= CommandHandler('hora', hora)
dispatcher.add_handler(manejadorHora)

updater.start_polling()

