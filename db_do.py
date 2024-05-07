# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-06 15:45

from db import DBTools

db_class = DBTools("127.0.0.1", 3306, "root", "admin123", "order_rpa")


def select_all(table):
    list1 = []
    a = db_class.execute(f"select * from {table};")
    print(a)
    for i_item in a:
        list1.append(i_item[1])
    return list1


def add_name(table, data_in):
    db_class.insert(table, data_in)


print(select_all('act_table'))
# add_name('act_table', {'name': 'pdf_act', 'skill_status': '未运行'})
