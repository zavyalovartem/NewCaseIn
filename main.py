from telegram.ext import Updater
from telegram.ext import CommandHandler
import os
import config

updater = Updater(token=config.TOKEN, use_context=True)
PORT = int(os.environ.get('PORT', '8443'))
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот Атом, если ты новый сотрудник "
                                                                    "корпорации как РосАтом, то я могу помочь тебе в "
                                                                    "адаптации в нашем большом и дружном коллективе)")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=config.TOKEN)
updater.bot.set_webhook(config.URL + config.TOKEN)
updater.idle()