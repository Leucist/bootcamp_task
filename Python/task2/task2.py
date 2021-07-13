from random import randint
import os   # used for a single system call only

# System call to fix the text colouring. Isn't necessary, feel free to remove ~
os.system("")

words = ["ЗИМА", "ЛЕТО", "ОСЕНЬ", "ВЕСНА", "ГОРДОСТЬ", "БЕЗУМИЕ", "ПРОГРАММИРОВАНИЕ", "ИГРА", "ЦИРКУМФЛЕКС", "РАДОСТЬ",
         "УНЫНИЕ", "АПАТИЯ", "КАТАРСИС", "ЛЕВ", "АНТИЛОПА"]
word = words[randint(0, 14)]
print(
    '''Добро пожаловать в игру \033[33m"Виселица"\033[0m!
Слово загадано, темы не будет. У Вас есть право на 10 ошибок. Удачи!\n'''
)
length = len(word)
lettersFound = []
lettersUsed = []


def game():
    placeholder = ""
    emptyPlaces = False
    for i in range(length):
        if word[i] in lettersFound:
            placeholder += word[i] + " "
        else:
            placeholder += "_ "
            emptyPlaces = True
    if not emptyPlaces:
        print("\033[33mСлово: " + placeholder)
        print("\033[32mВы победили! Поздравляем :Р\033[0m")
        exit(0)
    print("\n\033[33mСлово: " + placeholder, end="\n\n\033[34m")
    for i in range(1040, 1072):
        char = chr(i)
        if char in lettersUsed:
            char = "\033[31m" + char + "\033[34m"
        print("\t" + char, end="")
        print("\n") if i % 10 == 0 and i != 1040 and i != 1070 else "pass"
    answer = input("\n\n\033[0mВведите букву: ").upper()
    if len(answer) > 1:
        print("\033[31mПожалуйста, введите одну букву\033[0m")
        return 0
    if answer in lettersUsed:
        print("\033[35mВы уже использовали эту букву\033[0m")
        return 0
    lettersUsed.append(answer)
    if answer not in word:
        print("\033[31mНет такой буквы!\033[0m")
        return 1
    lettersFound.append(answer)
    print("\033[32mЕсть такая буква!\033[0m")
    return 0


if __name__ == '__main__':
    lose = False
    mistakes = 0
    while not lose:
        mistakes += game()
        print("\n"*5 + "Количество попыток: " + str(10 - mistakes))
        if mistakes == 10:
            lose = True
            print("\033[31mВы проиграли.\033[0m")
