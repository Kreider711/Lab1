# -*- coding: utf-8 -*-

li = [4,6,8,8,16,18,20]
n = 1


for i in range(len(li)-1):
    if li[i] > li[i+1]:
        flag = False
        break
    else:
        flag = True
    n += 1
     
print(flag)
    
input()

