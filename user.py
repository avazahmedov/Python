from datetime import datetime

def get_op():
    oper = int(input('Чтобы импортировать - 1\nЧтобы экспортировать - 2\nЧтобы удалить - 3\nЧтобы изменить - 4\nЧтобы получить весь список - 5\n '))
    return oper

def data_in():
    note_title = input('Введите заголовок заметки: ')
    note_msg = input('Введите текст заметки: ')
    note_id = input('Введите ID заметки: ')
    note_in = note_title + ' ' + note_msg + ' ' + note_id
    return note_in

def data_out():
    note_out = input('Введите одну из характеристик заметки: ')
    return note_out

def data_del():
    note_del = input('Введите одну из характеристик работника для удаления: ')
    return note_del

def data_change():
    note_change = input('Введите одну из характеристик работника для изменения: ')
    return note_change
