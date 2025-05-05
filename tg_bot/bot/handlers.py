from aiogram import Router, types
from aiogram.filters.command import Command
from bot.keyboards import models_keyboard, menu_keyboard, admin_keyboard
from config.settings import ADMINS

router = Router()

handlers_router = router

@handlers_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!")
    await cmd_menu(message)

@handlers_router.message(Command("admin"))
async def cmd_admin(message: types.Message):
    if message.from_user.id not in ADMINS:
        return await message.answer("Нет прав доступа!")
    await message.answer("Есть права доступа", reply_markup=admin_keyboard())

@handlers_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=menu_keyboard())

@handlers_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Это помощь.")

@handlers_router.message(Command("models"))
async def cmd_models(message: types.Message):
    await message.answer("Выберите модель:", reply_markup=models_keyboard())