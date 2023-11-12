# -*- coding: cp1251 -*
import random

on_game = 1
total = 0
session_total = 0
val_question = 0

dict_mean = {"Эйнштейн":"14.04.1879",
             "Ньютон":"25.12.1643",
             "Кюри":"7.11.1867",
             "Бонапарт":"15.08.1769",
             "Шекспир":"26.04.1564"}

dict_mean_symb = {"Эйнштейн":"Четырнадцатое апреля 1879 года",
             "Ньютон":"двадцать пятое декабря 1643 года",
             "Кюри":"седьмое ноября 1867 года",
             "Бонапарт":"пятнадцатое августа 1769 года",
             "Шекспир":"двадцать шестое апреля 1564 года"}

while on_game == 1:

    data = list(dict_mean.items())
    r_list = random.sample(data, 5)
    r_data = dict(r_list)

    for key, val in r_data.items():
        user_input = input("Введите дату рождения " + key + ": ")
        val_question += 1

        if (user_input == val):
            print("!!!Правильно!!!", end="\n\n")
            session_total += 1
        else:
            print("правильный ответ: " + dict_mean_symb[key], end="\n\n")


    if (val_question == 5):
        total += session_total

        print("=====================================", end="\n|\n")
        print("| правильных ответов в сессии:    " + str(session_total))
        print("| правильных ответов всего:       " + str(total), end="\n|\n")
        print("=====================================", end="\n\n")

        session_total = 0

        input_retry = input("Еще разок? \n1 = да\n2 = нет\n")
        if (on_game == int(input_retry)):
            val_question = 0

            print("\n")
            print("=====================================", end="\n")
            print("=====================================", end="\n\n")
            continue
        else:
            break

print("пока")
