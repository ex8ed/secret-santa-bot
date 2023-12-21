# -*- coding: UTF-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Buttons:
    REGISTRY = '👋 Регистрация'
    GET_MESSAGE = '📨 Мое задание'
    GET_HELP = '🆘 Помощь'
    GET_TRACKER = '🎫 Как там моя посылка?'
    SET_TRACKER = '📦 Заявить трекер'


btn_registry = KeyboardButton(Buttons.REGISTRY)
btn_get_message = KeyboardButton(Buttons.GET_MESSAGE)
btn_get_help = KeyboardButton(Buttons.GET_HELP)
btn_get_tracker = KeyboardButton(Buttons.GET_TRACKER)
btn_set_tracker = KeyboardButton(Buttons.SET_TRACKER)


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(btn_registry,
              btn_get_message,
              btn_get_help,
              btn_get_tracker,
              btn_set_tracker)
