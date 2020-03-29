# -*- coding: utf-8 -*-
sum = int(input('Ведите сумму'))
Bank1000 = 5
Bank100 = 8
Bank50 = 4
Bank10 = 6


tis = sum // 1000
sum = sum % 1000
if tis > Bank1000:
    print('Операция не может быть выполнена')
    print('В банкомате не достаточно средст')
else:
    sot = sum // 100
    sum = sum % 100
    if sot > Bank100:
         print('Операция не может быть выполнена')
         print('Введите сумму кратной 1000 ')
    else:
         polt = sum // 50
         sum = sum % 50
         if polt > Bank50:
             print('Операция не может быть выполнена')
             print('Введите сумму кратной 1000 или 100')
         else:      
             des = sum // 10
             if des > Bank10:
                 print('Операция не может быть выполнена')
                 print('Введите сумму кратной 1000 или 100 или 50')
             else:
                 print(tis, '* 1000 +',sot,'* 100 +',polt,'* 50 +', des, '* 10')
input()
