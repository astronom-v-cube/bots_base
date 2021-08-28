from telebot import types
from emoji import emojize

standart_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
standart_keyboard.add(emojize(":chart_increasing: Кнопка :chart_increasing:"))

commands_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
commands_keyboard.add(emojize(":bell: Подписаться :bell:")).add(emojize(":bell_with_slash: Отписаться :bell_with_slash:"), emojize(":cross_mark: Стоп :cross_mark:")).add(emojize(":warning: Баг-репорт :warning:"), emojize(":counterclockwise_arrows_button: В начало :counterclockwise_arrows_button:"))
