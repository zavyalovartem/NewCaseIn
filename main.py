from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import os

PORT = int(os.environ.get('PORT'))
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


CHOOSING_OPTION, MONTHLY_PAYMENT, YEARLY_PAYMENT, CARREER, QUIZES, OFFICES = range(6)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот Атом, если ты новый сотрудник "
                                                                    "корпорации как РосАтом, то я могу помочь тебе в "
                                                                    "адаптации в нашем большом и дружном коллективе)")
    #Добавление в бд
    markup = [
        ['Зарплата за месяц', 'Зарплата за год'],
        ['Твоя карьерная лестница'],
        ['Викторины по различным темам о нашей компании'],
        ['Карта офисов нашей компании']
    ]
    keyboard = ReplyKeyboardMarkup(markup, one_time_keyboard=False)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выбери, что ты хочешь узнать. В разделе \"инфа о "
                                                                    "нас\" есть сного важной и интересной информации "
                                                                    "о РосАтоме и опросы по ней. Лучших по ним ждут "
                                                                    "небольшие призы)", keyboard=keyboard)


def monthly_payment(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='35000 рублей')#Достать данные по зп из бд


def yearly_payment(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='420000 рублей')#Достать данные по зп из бд


def carreer(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='1,2,3,4(тут),5')#Достать из бд


def offices(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='')  # Достать из бд


dispatcher.add_handler(start)
dispatcher.add_handler(MessageHandler(Filters.regex('Зарплата за месяц$'), monthly_payment))
dispatcher.add_handler(MessageHandler(Filters.regex('Зарплата за год$'), yearly_payment))
dispatcher.add_handler(MessageHandler(Filters.regex('Твоя карьерная лестница$'), carreer))
dispatcher.add_handler(MessageHandler(Filters.regex('Карта офисов нашей компании$'), offices))


updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook(URL + TOKEN)
updater.idle()