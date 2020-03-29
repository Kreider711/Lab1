# -*- coding: utf-8 -*-
p1 = ""
p2 = ""
p3 = ""
p4 = ""
x = 0;
while True:
     try:
            x = str(input("Введите номер карты[16 цифр]="))
            if len(x)==16:
                break
            else:
                print ("Код не соответствует 16 значному")
     except ValueError:
            print ("Неверный формат")

p1 = x[0:4:1]
p2 = x[4:8:1]
p3 = x[8:12:1]
p4 = x[12:16:1]
print ("Номер:"+p1+" **** ****"+p4)
input()