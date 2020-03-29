# -*- coding: utf-8 -*-
import math

N1 = int(input('Какой размер массива ?\n'))

lg = math.log(N1, 2)
lg = math.ceil(lg)
lg = math.pow(2, lg)
N2 = int(lg)
print('Ближайший допустимы размер массива', N2)
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
