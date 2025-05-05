from aiogram import Router, F
from aiogram.types import Message
from bot.handlers import cmd_menu, cmd_models
from config.settings import PASSWORD, ADMINS
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.keyboards import admins_conrols_keyboard

router = Router()

button_router = router

# класс всех состояний 
class AdminStates(StatesGroup):
    warning_for_password = State()
    waiting_add_user_id = State()
    waiting_delete_user_id = State()


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
        await message.answer("Доступ разрешен", reply_markup=admins_conrols_keyboard())
        await state.clear()
    else:
        await message.answer("Неверный пороль")
        await state.clear()

@button_router.message(F.text == "Добавить")
async def add_admin_selected(message: Message, state: FSMContext):
       await message.answer("Введите ID пользователя lдля добавления")
       await state.set_state(AdminStates.waiting_add_user_id)

@button_router.message(F.text == "Удалить")
async def add_admin_selected(message: Message, state: FSMContext):
       await message.answer("Введите ID пользователя для удаления")
       await state.set_state(AdminStates.waiting_delete_user_id)

@button_router.message(AdminStates.waiting_add_user_id)
async def add_user_id(message: Message, state: FSMContext):
    user_id = int(message.text.strip())
    if user_id not in ADMINS:
        ADMINS.append(user_id)
        await message.answer(f"Пользователь {user_id} добавлен в админы")
    else:
        await message.answer("Этот пользователь уже есть")
    await state.clear

@button_router.message(AdminStates.waiting_delete_user_id)
async def delete_user_id(message: Message, state: FSMContext):
    user_id = int(message.text.strip())
    if user_id in ADMINS:
        ADMINS.remove(user_id)
        await message.answer(f"Пользователь {user_id} удалён из админов.")
    else:
        await message.answer("Этого пользователя нет в списке админов.")
    await state.clear()