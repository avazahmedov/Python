def get_op():
    oper = int(input('Чтобы импортировать - 1\nЧтобы экспортировать - 2\nЧтобы удалить - 3\nЧтобы изменить - 4\n '))
    return oper

def data_in():
    name_worker = input('Введите имя работника: ')
    lastname_worker = input('Введите фамилию работника: ')
    cell_worker = input('Введите номер телефона работника: ')
    worker_in = name_worker + ' ' + lastname_worker + ' ' + cell_worker
    return worker_in

def data_out():
    worker_out = input('Введите одну из характеристик работника: ')
    return worker_out

def data_del():
    worker_del = input('Введите одну из характеристик работника для удаления: ')
    return worker_del

def data_change():
    worker_change = input('Введите одну из характеристик работника для изменения: ')
    return worker_change
