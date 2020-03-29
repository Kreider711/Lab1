# -*- coding: utf-8 -*-
import random
import itertools
import datetime

teams = ['team1', 'team2', 'team3', 'team4',
        'team5', 'team6', 'team7', 'team8',
        'team9', 'team10', 'team11', 'team12',
        'team13', 'team14', 'team15', 'team16']

random.shuffle(teams)
print('Команды: ', teams)

plays = [teams[i:i + 4] for i in range(0, len(teams), 4)]
print('Группы:')
print(plays[0])
print(plays[1])
print(plays[2])
print(plays[3])

now_date = datetime.datetime.now()
now_date = now_date.replace(2020, 9, 14)

first_date = datetime.datetime(2020, 9, 20)
end_date = datetime.timedelta(days=14)
i = j = 0
print('Игры:')
while first_date <= datetime.datetime(2021, 4, 4):
    first_date += end_date
    if j < len(teams):
        print(first_date.day, '/', first_date.month, '/', first_date.year, ', 22:45, ', str(teams[i]), ' - ', str(teams[j + 1]))
        i += 1
        j += 1
input()