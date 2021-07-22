import telebot
import config
import json
from random import randint
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

words = ["ЗИМА", "ЛЕТО", "ОСЕНЬ", "ВЕСНА", "ГОРДОСТЬ", "БЕЗУМИЕ", "ПРОГРАММИРОВАНИЕ", "ИГРА", "ЦИРКУМФЛЕКС", "РАДОСТЬ",
         "УНЫНИЕ", "АПАТИЯ", "КАТАРСИС", "ЛЕВ", "АНТИЛОПА"]
# word = words[randint(0, 14)]
# length = len(word)
lettersFound = []
lettersUsed = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = l_markup()
    word = words[randint(0, 14)]
    length = len(word)
    stMsg = '''Привет, <b>{0.first_name}</b>!
Добро пожаловать в игру <b>"Виселица"</b>! Слово загадано, темы не будет. У Вас есть право на 10 ошибок.
Удачи!'''
    bot.send_message(message.chat.id, stMsg.format(message.from_user), parse_mode='html')
    sent = bot.send_message(message.chat.id, "Загаданное слово: " + "_ " * length, reply_markup=markup)
    bot.register_next_step_handler(sent, game, [word, length])


def l_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1040, 1072):
        char = chr(i)
        if char not in lettersUsed:
            markup.add(char)
    return markup


# нет обработки символов. Чтобы принимало только кириллицу
def game(message, args):
    word = args[0]
    length = args[1]
    placeholder = ""
    emptyPlaces = False
    for i in range(length):
        if word[i] in lettersFound:
            placeholder += word[i] + " "
        else:
            placeholder += "_ "
            emptyPlaces = True
    if not emptyPlaces:
        bot.send_message(message.chat.id, "Слово: " + placeholder)
        bot.send_message(message.chat.id, "Вы победили! Поздравляем :Р")
        return
    bot.send_message(message.chat.id, "Слово: " + placeholder)
    markup = l_markup()
    answer = message.text.upper()
    # answer = input("\n\n\033[0mВведите букву: ").upper()
    if len(answer) > 1:
        bot.send_message(message.chat.id, "Пожалуйста, введите одну букву")
        return 0
    if answer in lettersUsed:
        bot.send_message(message.chat.id, "Вы уже использовали эту букву")
        return 0
    lettersUsed.append(answer)
    if answer not in word:
        bot.send_message(message.chat.id, "Нет такой буквы!")
        return 1
    lettersFound.append(answer)
    bot.send_message(message.chat.id, "Есть такая буква!")
    return 0


def pre_game():
    lose = False
    mistakes = 0
    while not lose:
        mistakes += game()
        print("\n" * 5 + "Количество попыток: " + str(10 - mistakes))
        if mistakes == 10:
            lose = True
            print("\033[31mВы проиграли.\033[0m")


bot.polling(none_stop=True)
