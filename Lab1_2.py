# -*- coding: utf-8 -*-

li = [4,6,8,8,16,18,20]
n = 1
flag = 1

for i in range(len(li)-1):
    if li[i] > li[i+1]:
        flag = 0
        break
    else:
        flag = 1
    n += 1
     
if flag==0:
    print ("FALSE")
else:
    print ("TRUE")
    
input()

