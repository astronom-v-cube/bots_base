from config import *
from astro_bot_vars import *
from db_functions import *
from sending_functions import *
import telebot
from keyboards import *

bot = telebot.TeleBot(main_token)

print('Лонгпул запущен...')

@bot.message_handler(func = lambda message: message.text.lower() in ["/subscribe", "подписаться", emojize(":bell: подписаться :bell:")])

def subscribe(message):

    send(message.from_user.id, 'Текст', subscribe_keyboard)

    bot.register_next_step_handler(message, subscribe_get_degree)  # следующий шаг – функция get_name

def subscribe_get_degree(message):

    if message.text.lower() in [emojize("Развилка")]:

        send(message.chat.id, 'Текст', standart_keyboard)

    elif message.text.lower() in [emojize("Развилка")]:

        send(message.chat.id, 'Текст', standart_keyboard)

    else:

        insert_into_db(message.from_user.id, var)


@bot.message_handler(func = lambda message: message.text.lower() in ["/unsubscribe", "отписаться", emojize(":bell_with_slash: отписаться :bell_with_slash:")])

def unsubscribe(message):

    send(message.from_user.id, 'Текст', subscribe_keyboard)

    bot.register_next_step_handler(message, unsubscribe_get_degree)

def unsubscribe_get_degree(message):

    if message.text.lower() in [emojize("Развилка")]:

        send(message.chat.id, 'Текст', standart_keyboard)

    else:

        delete_from_db(message.from_user.id, var)


@bot.message_handler(func = lambda message: message.text.lower() in ["/bugreport", "помощь", emojize(":warning: баг-репорт :warning:"), "багрепорт", "баг-репорт"])

def bugreport(message):

    send(message.from_user.id, 'Пожалуйста, опишите проблему', types.ReplyKeyboardRemove())

    bot.register_next_step_handler(message, get_bugreport)  # следующий шаг – функция get_name

def get_bugreport(message):

    send(792302351, f'{emojize(":warning: Баг-репорт :warning:")}\nТекст баг-репорта: {message.text}\nОтправитель: {message.from_user.id}', None)
    send(message.chat.id, 'Ваш баг-репорт отправлен разработчику бота, в ближайшее время он займется исправлением неисправности. Спасибо :)', standart_keyboard)


@bot.message_handler(func = lambda message: message.text.lower() in ["/admin"])

def admin_send(message):

    send(message.from_user.id, 'ID пользователя: ...', types.ReplyKeyboardRemove())

    bot.register_next_step_handler(message, get_send_id)  # следующий шаг – функция get_name

def get_send_id(message):

    global id
    id = message.text

    send(message.from_user.id, 'Текст сообщения для пользователя: ...', None)

    bot.register_next_step_handler(message, get_send_msg)  # следующий шаг – функция get_name


def get_send_msg(message):

    text = message.text

    send(id, text, standart_keyboard)
    send(message.from_user.id, 'Сообщение отправлено', standart_keyboard)


@bot.message_handler(content_types=["text"])

def send_text(message):
    if message.text.lower() in ['старт', 'начать', 'привет', '/start']:

        send(message.chat.id, hello, standart_keyboard)

    elif message.text.lower() in ['команды', '/help', emojize(":memo: команды :memo:")]:

        send(message.chat.id, commands, commands_keyboard)

    elif message.text.lower() in ['в начало', emojize(":counterclockwise_arrows_button: в начало :counterclockwise_arrows_button:")]:

        send(message.chat.id, 'Текст', standart_keyboard)

    elif message.text.lower() in ['/stop', 'стоп', emojize(":cross_mark: стоп :cross_mark:")]:

        delete_from_db_for_id(message.chat.id)

def job_longpool():

    bot.infinity_polling()
