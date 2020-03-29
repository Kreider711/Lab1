# -*- coding: utf-8 -*-
def get_frames(signal, size, overlap):
    signal = [x for x in range(0, size)]
    frame = 5
    print('Размер фрейма(окна): ', frame)
    step = frame * overlap
    print('Шаг: ',step)
    i = 0
    while i < len(signal):
        yield (signal[i:i + frame])
        i += int(step)

signal = []
print('Оконная декомпозиция:')
for frame in get_frames(signal, size=10, overlap=0.25):
    print(frame)
input()