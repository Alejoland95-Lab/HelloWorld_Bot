import os
from telegram.ext import Updater, CommandHandler

# Leemos el TOKEN desde las variables de entorno
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("No se encontró el TOKEN en las variables de entorno.")

# Función que responde al comando /start
def start(update, context):
    update.message.reply_text("Hola mundo")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(CommandHandler("start", start))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()