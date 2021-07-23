import asyncio
import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint


words = ["ЗИМА", "ЛЕТО", "ОСЕНЬ", "ВЕСНА", "ГОРДОСТЬ", "БЕЗУМИЕ", "ПРОГРАММИРОВАНИЕ", "ИГРА", "ЦИРКУМФЛЕКС", "РАДОСТЬ",
         "УНЫНИЕ", "АПАТИЯ", "КАТАРСИС", "ЛЕВ", "АНТИЛОПА"]
lettersFound = []
lettersUsed = []
mistakes = 0
word = ""


logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Word(StatesGroup):
    letter = State()


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    global word, lettersFound, lettersUsed, mistakes
    lettersFound, lettersUsed, mistakes = [], [], 0
    word = words[randint(0, 14)]
    length = len(word)
    stMsg = '''Привет, <b>{0.first_name}</b>!
Добро пожаловать в игру <b>"Виселица"</b>! Слово загадано, темы не будет. У Вас есть право на 10 ошибок.
Удачи!'''
    await bot.send_message(message.chat.id, stMsg.format(message.from_user), parse_mode='html')
    await pre_game(message.chat.id)


def l_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # костыль :P
    # arr, row1, row2, row3 = [], [], [], []
    for i in range(1040, 1072):
        char = chr(i)
        if char not in lettersUsed:
            markup.add(char)
            
            # Красиво пока не очень работает~
    #         arr.append(KeyboardButton(char))
    # i = 0
    # while i <= len(arr) and i <= 10:
    #     row1.append(arr[i])
    #     i += 1
    # while i <= len(arr) and i <= 20:
    #     row2.append(arr[i])
    #     i += 1
    # while i <= len(arr) and i <= 31:
    #     row3.append(arr[i])
    #     i += 1
    # markup.row(row1)
    # markup.row(row2)
    # markup.row(row3)
    return markup


async def pre_game(msgId):
    await bot.send_message(msgId, "- " * 16 + "\nКоличество попыток: " + str(10 - mistakes))
    if mistakes == 10:
        lose = True
        await bot.send_message(msgId, "Вы проиграли.")
    elif mistakes < 0:
        lose = True
    await game(msgId)


# нет обработки символов. Чтобы принимало только кириллицу
async def game(msgId):
    placeholder = ""
    emptyPlaces = False
    for i in range(len(word)):
        if word[i] in lettersFound:
            placeholder += word[i] + " "
        else:
            placeholder += "_ "
            emptyPlaces = True
    if not emptyPlaces:
        await bot.send_message(msgId, "Слово: " + placeholder)
        await bot.send_message(msgId, "Вы победили! Поздравляем :Р")
        global mistakes
        mistakes -= 100
    markup = l_markup()
    await bot.send_message(msgId, "Загаданное слово: " + placeholder, reply_markup=markup)
    await Word.letter.set()


@dp.message_handler(state=Word.letter)
async def check_answer(message: types.Message, state: FSMContext):
    answer = message.text.upper()
    await state.update_data(letter=answer)
    global mistakes
    if len(answer) > 1:
        await bot.send_message(message.chat.id, "Пожалуйста, введите одну букву")
        await pre_game(message.chat.id)
        return
    if answer in lettersUsed:
        await bot.send_message(message.chat.id, "Вы уже использовали эту букву")
        await pre_game(message.chat.id)
        return
    lettersUsed.append(answer)
    if answer not in word:
        await bot.send_message(message.chat.id, "Нет такой буквы!")
        mistakes += 1
        await pre_game(message.chat.id)
        return
    lettersFound.append(answer)
    await bot.send_message(message.chat.id, "Есть такая буква!")
    await pre_game(message.chat.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
