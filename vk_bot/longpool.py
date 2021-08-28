#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import schedule
import urllib.request
import urllib3
import requests
import socket
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import *
from bot_vars import *

socket.setdefaulttimeout(60)

print ('Бот запущен...')

vk_session = VkApi(token = main_token)
vk = vk_session.get_api()

# функция прослушивания longpoll и ответа на ключевые слова
def job_longpool():
    print('Функция прослушивания longpool запущена')
    longpoll = VkBotLongPoll(vk_session, 'number_group')
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print('-' * 30)
                    print(f'Сообщение получено от id: ' + str({event.obj["peer_id"]}) )
                    print('-' * 30)
                    print('Текст сообщения: ' + str(event.object['text']))
                    print('-' * 30)

                    msg = event.object['text'].lower()
                    id = event.obj["peer_id"]

                    if msg in ('начать', 'привет', 'старт'):
                        send (event, hello, keyboard)

                    elif msg in ('test', 'тест'):
                        send (event, 'Бот работает успешно!', keyboard)

                    elif msg in ('команды', 'commands'):
                        send (event, commands, keyboard_two)

                    elif msg in ('багрепорт', 'баг-репорт', 'баг'):
                        send (event, 'Если с ботом возникли какие-то проблемы, вы можете сообщить о них разработчику. Для этого напишите в одном сообщении: сначала слово "помощь", а затем опишите неполадку. Ваше сообщение будет отправлено разработчику бота', keyboard)

                    elif 'помощь' in msg or 'help' in msg:
                        vk.messages.send(random_id = get_random_id(), peer_id = 557660245, message = (f'&#10071;БАГ-РЕПОРТ&#10071; {event}'))
                        send (event, 'Ваш баг-репорт отправлен разработчику бота, в ближайшее время он займется исправлением неисправности. Спасибо :)', keyboard)

                    elif msg in ('stop', 'стоп'):
                        delete_from_db_for_id(id, keyboard)

                    elif msg == 'Скинь фотку':
                        img = urllib.request.urlopen(url_picture_1, timeout = 30).read()
                        out = open("Primary.png", "wb")
                        out.write(img)
                        out.close()
                        upload = vk_api.VkUpload(vk)
                        photo = upload.photo_messages('Primary.png')
                        owner_id = photo[0]['owner_id']
                        photo_id = photo[0]['id']
                        access_key = photo[0]['access_key']
                        attachment = f'photo{owner_id}_{photo_id}_{access_key}'

                        send_attachment (event, attachment, keyboard)

                    else:
                        if not event.from_chat:
                            send(event, 'К сожалению, я не понимаю...(', keyboard)

        except (socket.timeout, urllib3.exceptions.ReadTimeoutError, requests.exceptions.ReadTimeout) as err:
            print(err)
            print('Переподключение longpool')
            longpoll = VkBotLongPoll(vk_session, '202712381')
