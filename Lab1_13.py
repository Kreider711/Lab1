# -*- coding: utf-8 -*-
from decimal import Decimal

def extra_enumerate(arr):
    st = 0
    soom = 0
    for elem in arr:
        yield elem
        st += 1
        soom = soom + elem
        frac = soom * 0.1
        frac = Decimal(frac)
        frac = frac.quantize(Decimal("1.0"))
        print('(', elem, ', ', soom,', ', frac,')')

x = [1, 5, 6, 2]
for i in extra_enumerate(x):
    print(end='')
input()

