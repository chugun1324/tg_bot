from aiogram import Router, F
from aiogram.types import Message
from bot.handlers import cmd_menu, cmd_models
from config.settings import PASSWORD
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

button_router = router

class AdminStates(StatesGroup):
    warning_for_password = State()

# menu
@button_router.message(F.text == "Выбор модели")
async def input_model_selected(message: Message):
    await cmd_models(message)

@button_router.message(F.text == "Помощь")
async def help_selected(message: Message):
    await message.answer("Это помощь.")

@button_router.message(F.text == "Премиум")
async def premium_selected(message: Message):
    await message.answer("...")

# models
@button_router.message(F.text == "GPT-3.5")
async def gpt35_selected(message: Message):
    await message.answer("Вы выбрали GPT-3.5")

@button_router.message(F.text == "Claude")
async def Claude_selected(message: Message):
    await message.answer("Вы выбрали Claude")

@button_router.message(F.text == "Назад")
async def close_selected(message: Message):
    await cmd_menu(message)

# admin panel

# control admins
@button_router.message(F.text == "Управление админами")
async def req_admin_selected(message: Message, state: FSMContext):
    await message.answer("Введите пороль: ")
    await state.set_state(AdminStates.warning_for_password) 

@button_router.message(AdminStates.warning_for_password)
async def check_password(message:Message, state: FSMContext):
    if message.text == PASSWORD:
        await message.answer("Доступ разрешен")
        # ...
        
    else:
        await message.answer("Неверный пороль")
        await state.clear()
