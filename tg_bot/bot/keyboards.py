from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

def models_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="GPT-3.5")
    kb.button(text="Claude")
    kb.button(text="Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def menu_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Выбор модели")
    kb.button(text="Премиум")
    kb.button(text="Помощь")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def admin_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Управление premium")
    kb.button(text="Бан User")
    kb.button(text="Кол-во Users")
    kb.button(text="Запросы к API")
    kb.button(text="Жалобы")
    kb.button(text="Управление админами")
    kb.button(text="Назад")

    kb.adjust(2, 2, 2, 1)
    return kb.as_markup(resize_keyboard=True)

def admins_conrols_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Добавить")
    kb.button(text="Удалить")
    kb.button(text="Назад")
    kb.adjust(2, 1)
    return kb.as_markup(resize_keyboard=True)