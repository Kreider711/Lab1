# -*- coding: utf-8 -*-
def non_empty(func):
    def wrapper():
        my_list = func()
        print('Начальная строка: ', my_list)
        my_list = list(filter(None, my_list))
        print('Полные строки: ', my_list)
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', '']

get_pages()
input()