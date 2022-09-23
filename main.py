# -*- coding: utf-8 -*-
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")

async def echo(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
if __name__ == '__main__':
    application = ApplicationBuilder().token('5622747333:AAEuq65UYrETg8kVUdAsJVxZJ5LjqgXQG9g').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
    
