"""
This is a krill-lotin bot.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin, to_cyrillic

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm krill-lotin-krill bot")



@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isascii():
        result = to_cyrillic(message.text)
    else:
        result = to_latin(message.text)

    await message.answer(result)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)