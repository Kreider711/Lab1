# -*- coding: utf-8 -*-
from decimal import Decimal

def frange(start, stop, step): 
    step = Decimal(step)    
  
    while start < stop: 
        start = Decimal(start)
        start = start.quantize(Decimal("1.0"))      
        print(start)
        start = start + step
         
frange(int(input('от ')),int(input('до ')),float((input('шаг'))))
       
input()