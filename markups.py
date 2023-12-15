# -*- coding: UTF-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_get_message = KeyboardButton('📨Мое задание')
btn_get_tracker = KeyboardButton('🎫Как там моя посылка?')
btn_get_help = KeyboardButton('🆘Помощь')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(btn_get_message, btn_get_tracker, btn_get_help)
