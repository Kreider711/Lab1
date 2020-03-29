# -*- coding: utf-8 -*-
stroka = input("Введите строку=")
mass = []
i = 0
while i<255:
    mass.append(0)
    i+=1
    
i = 0
for k in stroka:
    mass[ord(k)] +=1 

    
i = 0
while i<255:
    if (mass[i]==1):
        print (chr(i))
    i+=1
    
input()