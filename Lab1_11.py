def frange(start, end, step):
    while start < end:
        yield round(start, 3)
        start += step

for f in frange(1, 5, 0.1):
    print(f)
    
input()