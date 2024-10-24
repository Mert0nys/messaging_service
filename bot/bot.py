import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = '8119584526:AAEh2nxuBJd7J27CQ8E8IgaQT93SBWtLBAE'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для уведомлений о новых сообщениях.")

async def on_startup(dispatcher):
    print("Бот запущен и готов к работе!")

async def on_shutdown(dispatcher):
    await bot.session.close()  # Закрытие сессии для диспатчера

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)