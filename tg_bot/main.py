import asyncio
from aiogram import Bot, Dispatcher
from config.settings import TOKEN
from bot.handlers import handlers_router
from bot.button import button_router
import logging

logging.basicConfig(level=logging.INFO) # включаем логирование

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(handlers_router)
    dp.include_router(button_router)
    print("бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())