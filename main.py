# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
#   1. Программа должна выводить данные
#   2. Программа должна сохранять данные в
# текстовом файле
#   3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
#   4. Использование функций. Ваша программа
# не должна быть линейной

from user import *
from data import *

while True:
    op = get_op()
    if op == 1:
        workerIn = data_in()
        write_data(workerIn)
    elif op == 2:
        opros2 = data_out()
        content = read_data()
        print(find_data(content, opros2))
    elif op == 3:
        opros3 = data_del()
        content = read_data()
        delete_data(content, opros3)
    elif op == 4:
        opros4 = data_change()
        content = read_data()
        change_data(content, opros4)
    else: break
