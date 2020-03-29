# -*- coding: utf-8 -*-
predlojenie = ""
mass = []



while True:
     try:
            predlojenie = str(input("Ведите предложение="))
            if len(predlojenie)!=0:
                break
            else:
                print ("Необходимо ввести предложение")
     except ValueError:
            print ("Некорректное предложение")

mass = predlojenie.split(' ')
print ([str(k) for k in mass])

n = 1 
while n < len(mass):
     for i in range(len(mass)-n):
          if len(mass[i]) < len(mass[i+1]):
               mass[i],mass[i+1] = mass[i+1],mass[i]
     n += 1
     
n = 0;

while n<len(mass):
        print (mass[n])
        n+=1
input()