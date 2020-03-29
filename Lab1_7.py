# -*- coding: utf-8 -*-
stroka = input("Введите Url=")

if stroka.find("http://")!=-1:
    print (stroka)
    if (stroka.find(".com",len(stroka)-4)==-1):
        stroka += ".com"
        print (stroka)

if stroka.find("www")!=-1 and stroka.find("http://")==-1:
    stroka = "http://"+stroka
    print (stroka)
    if (stroka.find(".com",len(stroka)-4)==-1):
        stroka += ".com"
        print (stroka)
input()