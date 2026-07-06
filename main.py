import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("🧠 AI Совет запущен. Напиши вопрос.")

@dp.message()
async def answer(message: types.Message):
    await message.answer(
        "📌 Я получил твой вопрос:\n\n" + message.text +
        "\n\n🤖 Пока работаю в базовом режиме"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
