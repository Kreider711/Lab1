# -*- coding: utf-8 -*-

strin = input('Введите строку: ')

for i in strin:
    spis = strin.split(" ")

for i in range(len(spis)):
    upp = ''.join(spis[i])    
    if upp.islower(): 
      i
    else:
        spis[i] = upp.upper()     
     
   
delimiter = " "
strin2 = delimiter.join(spis)
print(strin2)
input()