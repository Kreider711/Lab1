sum = int(input('Ведите сумму'))
Bank = dict({1000:int(5), 100:8, 50:4, 10:6})

tis = sum // 1000
sum = sum % 1000

if Bank[1000] < tis:
    print('Операция не может быть выполнена')
    print('В банкомате не достаточно средст')
else:
    sot = sum // 100
    sum = sum % 100
    if Bank[100] < sot:
         print('Операция не может быть выполнена')
         print('Введите сумму кратной 1000 ')
    else:
         polt = sum // 50
         sum = sum % 50
         if Bank[50] < polt:
             print('Операция не может быть выполнена')
             print('Введите сумму кратной 1000 или 100')
         else:      
             des = sum // 10
             if Bank[10] < des:
                 print('Операция не может быть выполнена')
                 print('Введите сумму кратной 1000 или 100 или 50')
             else:
                 print(tis, '* 1000 +',sot,'* 100 +',polt,'* 50 +', des, '* 10')
input()
