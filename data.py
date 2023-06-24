def write_data(note):
    with open ('baza.txt', 'a') as baza:
        baza.write(note + '\n')
    

def read_data ():
    with open ('baza.txt', 'r') as baza:
        content = baza.readlines()
        return content


    

def find_data(lst, str):
    for value in lst:
        if str in value:
            return value        


def delete_data(lst, str):
    lst1 = []
    with open ('baza.txt', 'r+') as baza:        
        for value in lst:
            if str in value:
                lst1.append(value)
    if len(lst1)>1:
        print(*lst1, sep='')
        dell = int(input('Какую строку вы хотите удалить? ')) - 1
        with open ('baza.txt', 'w') as baza:
            for value in lst:
                if lst1[dell] not in value:
                    baza.write(value)
            baza.write('')
    else: 
        with open ('baza.txt', 'w') as baza:
            for value in lst:
                if str not in value:
                    baza.write(value)
            baza.write('')
    

def change_data(lst, str):
    lst1 = []
    with open ('baza.txt', 'r+') as baza:        
        for value in lst:
            if str in value:
                lst1.append(value)
    if len(lst1)>1:
        print(*lst1, sep='')
        dell = int(input('Какую строку вы хотите изменить? ')) - 1
        new_change = input('Введите новую строку: ') + '\n'
        with open ('baza.txt', 'w') as baza:
            for value in lst:
                if lst1[dell] in value:
                    value = new_change
                baza.write(value)
            baza.write('')
    else:
        print(*lst1)
        new_change = input('Введите новую строку: ')  + '\n'
        with open ('baza.txt', 'w') as baza:
            for value in lst:
                if str in value:
                    value = new_change 
                baza.write(value)
            baza.write('')    