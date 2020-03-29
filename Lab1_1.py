# -*- coding: utf-8 -*-

def format(x):
    x = str(x)
    if (len(x)<2):
        x = str(x+"0")
    return x
money = 0
real = 0
coins = 0

while True:
     try:
            money = float(input("Введите число которое необходимо преобразовать"))
            if money>0:
                break
            else:
                print ("Некорректный формат")
     except ValueError:
            print ("Некорректный формат")

if (str(money)).find(".")!=-1:
    money = (str(money)).split(".")
    real = money[0]
    coins = format(money[1])
else:
    real = money
    coins = "00"
print (real+"p. "+coins+"kop.")

input()