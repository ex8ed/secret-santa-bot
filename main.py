# -*- coding: UTF-8 -*-
import os
import logging
from time import localtime, strftime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import config
import markups as nav
from db import Database

load_dotenv()
token = os.getenv('TOKEN')

console_out = logging.StreamHandler()
file_log = logging.FileHandler("bot-info.log")
logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)


bot = Bot(token)
dp = Dispatcher(bot)
db = Database('database.db')


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    if not db.user_exists(msg.from_user.id):
        db.add_user(msg.from_user.id)
        logging.info(config.new_user % (strftime(config.time_format, localtime()), msg.from_user.id))
        await bot.send_message(msg.from_user.id, config.start_message, reply_markup=nav.main_menu)
    else:
        await bot.send_message(msg.from_user.id, config.usr_exists_message, reply_markup=nav.main_menu)


@dp.message_handler()
async def communication(msg: types.Message):
    if msg.chat.type == 'private':
        if msg.text == '👋 Регистрация':
            # TODO: test registration functionality before pushing
            if db.get_signup(msg.from_user.id) == 'setvkid':
                await bot.send_message(msg.from_user.id, config.registration_message)
                if config.is_allowed(msg.text):
                    db.set_vk_id(msg.from_user.id, msg.text)
                    db.set_signup(msg.from_user.id, 'complete')
                    logging.info(config.new_user % (strftime(config.time_format, localtime()),
                                                    msg.from_user.id,
                                                    msg.text))
                    await bot.send_message(msg.from_user.id, config.registration_success, reply_markup=nav.main_menu)
                else:
                    await bot.send_message(msg.from_user.id, config.registration_failed)
            else:
                await bot.send_message(msg.from_user.id, config.registration_already, reply_markup=nav.main_menu)
        elif msg.text == '📨 Мое задание':
            # TODO: check for being registered
            ...
        elif msg.text == '🎫 Как там моя посылка?':
            # TODO: check for being registered
            ...
        elif msg.text == '📦 Заявить трекер':
            # TODO: check for being registered
            ...
        elif msg.text == '🆘 Помощь':
            await bot.send_message(msg.from_user.id, config.help_message, reply_markup=nav.main_menu)
        else:
            await bot.send_message(msg.from_user.id, config.default_message, reply_markup=nav.main_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
