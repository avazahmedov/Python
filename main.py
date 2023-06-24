import datetime
import user

from user import *
from data import *
from datetime import datetime

while True:
    op = get_op()
    if op == 1:
        noteIn = data_in()
        write_data(noteIn)
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
    elif op == 5:
        lst = read_data()
        print(lst)
    else: break
