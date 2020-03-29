def extra_enumerate(x):
    cum = 0
    full_cum = sum(x)
    for i in x:
        cum += i
        frac = round(cum / full_cum, 1)
        yield i, cum, frac


lst = [1, 2, 4, 3]
for elem, cum, frac in extra_enumerate(lst):
    print("({}, {}, {})".format(elem, cum, frac), end="\n" )
    
input()



