# -*- coding: UTF-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# TODO: make objects with button namings
btn_registry = KeyboardButton('👋 Регистрация')
btn_get_message = KeyboardButton('📨 Мое задание')
btn_get_help = KeyboardButton('🆘 Помощь')
btn_get_tracker = KeyboardButton('🎫 Как там моя посылка?')
btn_set_tracker = KeyboardButton('📦 Заявить трекер')


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(btn_registry,
              btn_get_message,
              btn_get_help,
              btn_get_tracker,
              btn_set_tracker)
