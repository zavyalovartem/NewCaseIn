from telegram.ext import Updater
from telegram.ext import CommandHandler
import os
import config

PORT = int(os.environ.get('PORT'))
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот Атом, если ты новый сотрудник "
                                                                    "корпорации как РосАтом, то я могу помочь тебе в "
                                                                    "адаптации в нашем большом и дружном коллективе)")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook(URL + TOKEN)
updater.idle()