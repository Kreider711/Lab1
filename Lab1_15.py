# -*- coding: utf-8 -*-
def pre_process(a):
    def decorator(func):
        def wrapper(s):
            print('Исходный список:')
            func(s)
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i - 1]
                s[i] = round(s[i], 5)
            print('\nЦифровая фильтрация списка: ')
            for sample in s:
                print(sample, '', end='')
        return wrapper
    return decorator

@pre_process(a=0.24)
def plot_signal(s):
    for sample in s:
        print(sample,'', end='')

s = [2,3,6,9,11,15,66,52]
plot_signal(s)
input()