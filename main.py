# -*- coding: UTF-8 -*-
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import markups as nav



load_dotenv()
token = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
