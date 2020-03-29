# -*- coding: utf-8 -*-
stroka = ('www.vk.com', 'www.odn', 'www.mail.ru', 'google')

for s in stroka:
    s = str(s)
    if s.startswith('www.', 0, 4):
        s = 'http://' + s
        if s.endswith('.com'):
            print(s)
        else:
            s = s + '.com'
            print(s)
input()