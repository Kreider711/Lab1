# -*- coding: utf-8 -*-
import random
import datetime
import itertools

teams = ['Барселона', 'Ювентус', 'Реал Мадрид', 
         'Манчестер Юнатед', 'Россия', 'Челси',
         'Арсенал', 'Ливерпуль', 'Зенит', 
         'Милан', 'Шахтер', 'Динамо', 
         'Лион', 'Бавария', 'Турция', 'Португалия']
random.shuffle(teams)
teams = [teams[i*4:i*4+4] for i in range(0, 4)]
groups = [i for i in itertools.combinations(teams, 4)]
[print('Группа №', i+1, groups[0][i]) for i in range(0, 4)]

now = datetime.datetime.now()
start = datetime.datetime(now.year, 9, 14, 22, 45)
for i in range(1, 16):
    print('Игра №', i, start.strftime('%d/%m/%Y %H:%M'))
    start += datetime.timedelta(days=14)
input()