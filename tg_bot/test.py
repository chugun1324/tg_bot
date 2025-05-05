import asyncio # для асинхронности 
import logging # для логирования 
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command # оброботка команд (start ... )
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import (Bold, as_list, as_marked_section, as_key_value, HashTag)
logging.basicConfig(level=logging.INFO) # включаем логирование

# для бота можно настроить конфиг вывода текста пример
# bot = Bot(
#     token="MY_COKEN"
#     default=DefaultBotProperties(
#         ParseMode=ParseMode.HTML
#         # ....
#     )
# )

bot = Bot(token="8102064308:AAF7kIbtPD13LTxJaFMjkiljUnqE1IleDNk")

dp = Dispatcher() # обробатывает все события или же апдейты 

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Чебупиццаа")],
        [types.KeyboardButton(text="Не чебупицца")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбирите способ подачи"
        )
    await message.answer("тебя зовут ?", reply_markup=keyboard)

@dp.message(Command("test")) # в декаратор ставим оброботчик чего-либо (к примеру команд)
async def cmd_start(message: types.Message):
    await message.reply("Test 1")

async def test_2(message: types.Message):
    await message.reply("Test 2")

dp.message.register(test_2, Command("test2")) # можно заносить вручную без декоратора 

@dp.message(Command('dice'))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("text"))
async def any_message(message: types.Message):
    await message.answer(
        "Hello, <b>world \n</b>" \
        f"<i>you super {message.from_user.full_name}</i>",
        parse_mode=ParseMode.HTML # вывод текста в виде HTML
    )
# есть встренные фоматы вывода текста к примеру списки 
@dp.message(Command("list"))
async def cmd_list(message: types.Message):
    content = as_list(
        as_marked_section(
            Bold("Succes: "),
            "Value 1",
            "Value 2",
            marker="✅ ",
        ),
        as_marked_section (
            Bold("Failed: "),
            "Value 1",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("SUBD: "),
            as_key_value("Total", 23),
            as_key_value("Acces", 12),
            marker=" ",
        ),
        HashTag("#list"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs()) # распоковка словоря

# проверка ошибки ввода команды 
@dp.message(Command("error"))
async def cmd_error(message: types.Message, command: Command):
    if command.arrgs is None:
        await message.answer("Нет аргумнта /?")
        return
    try:
        pass
    except ValueError:
        await message.answer("Ошибка")
        return
    await message.answer("Все оке")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())