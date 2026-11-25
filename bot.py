import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("8605210560:AAGPGgIeHN9cL27RrP0lPCSckl5R0YOfUJc")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        "Я простой бот. Напиши что-нибудь — я отвечу эхом.\n"
        "Команды: /start, /help"
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start — приветствие\n"
        "/help — это сообщение\n\n"
        "Любой другой текст — верну его обратно."
    )


@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не задан. Установи переменную окружения BOT_TOKEN.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
