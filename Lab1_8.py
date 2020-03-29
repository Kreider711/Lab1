# -*- coding: utf-8 -*-

N1 = int(input('Какой размер массива ?\n'))

I = N1
r = int(1)
i = 0

while i < 1:
    p = 2 ** r
    
    if I > p:
        r += 1
    else:
        N2 = 2** r
        print('Будет массив из ', N2,'элементов ')
        i = i + 1
        
C = N2
mas = []
E = 0
from random import randint
for i in range(C):
    if i < N1:        
        mas.append( randint(1, 1000))
    else:
         mas.append(0)
         
print(mas)

input()
