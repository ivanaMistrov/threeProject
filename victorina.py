# -*- coding: cp1251 -*
import random

on_game = 1
total = 0
session_total = 0
val_question = 0

dict_mean = {"��������":"14.04.1879",
             "������":"25.12.1643",
             "����":"7.11.1867",
             "��������":"15.08.1769",
             "�������":"26.04.1564"}

dict_mean_symb = {"��������":"������������� ������ 1879 ����",
             "������":"�������� ����� ������� 1643 ����",
             "����":"������� ������ 1867 ����",
             "��������":"����������� ������� 1769 ����",
             "�������":"�������� ������ ������ 1564 ����"}



temp_dict_mean_symb = list(dict_mean_symb.values())
print(temp_dict_mean_symb)



while on_game == 1:

    data = list(dict_mean.items())
    r_list = random.sample(data, 5)
    r_data = dict(r_list)

    for key, val in r_data.items():
        user_input = input("������� ���� �������� " + key + ": ")
        val_question += 1

        if (user_input == val):
            print("!!!���������!!!", end="\n\n")
            session_total += 1
        else:
            print("���������� �����: " + dict_mean_symb[key], end="\n\n")


    if (val_question == 5):
        total += session_total

        print("=====================================", end="\n|\n")
        print("| ���������� ������� � ������:    " + str(session_total))
        print("| ���������� ������� �����:       " + str(total), end="\n|\n")
        print("=====================================", end="\n\n")

        session_total = 0

        input_retry = input("��� �����? \n1 = ��\n2 = ���\n")
        if (on_game == int(input_retry)):
            val_question = 0

            print("\n")
            print("=====================================", end="\n")
            print("=====================================", end="\n\n")
            continue
        else:
            break

print("����")
