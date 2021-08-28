from db_functions import *
from keyboards import *
from config import *
import vk_api
from vk_api.utils import get_random_id


bot = telebot.TeleBot(main_token)

# функция отправки текстового сообщения
def send(event, msg, kbd):

    if event.obj['peer_id'] > 2e9:       #если чат
        print(f'Ответил: "{msg}" для беседы с id: {event.obj["peer_id"]}')
        return vk.messages.send(random_id = get_random_id(), peer_id = event.obj['peer_id'], message = msg)
    else:
        print(f'Ответил: "{msg}" для пользователя с id: {event.obj["peer_id"]}')
        return vk.messages.send(random_id = get_random_id(), peer_id = event.obj['peer_id'], keyboard = kbd.get_keyboard(), message = msg)


# функция отправки сообщения с фото
def send_attachment(event, image, kbd):

    if event.obj['peer_id'] > 2e9:       #если чат
        print(f'Отправил фото для беседы с id: {event.obj["peer_id"]}')
        return vk.messages.send(random_id = get_random_id(), peer_id = event.obj['peer_id'], attachment = image)
    else:
        print(f'Отправил фото для пользователя с id: {event.obj["peer_id"]}')
        return vk.messages.send(random_id = get_random_id(), peer_id = event.obj['peer_id'], keyboard = kbd.get_keyboard(), attachment = image)


# функция рассылки оповещения
def sending(var):

    list_id = search_into_db(var)

    for id_one in list_id:
        vk.messages.send(random_id = get_random_id(), peer_id = id_one, keyboard = keyboard.get_keyboard(), message = f'&#10071;Внимание!&#10071;')

    print(f'Выполнил рассылку')
