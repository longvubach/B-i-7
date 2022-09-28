
import random
def ngaunhien(n,min,max):
    if max - min >= n:
        if min > max:
            c = min
            min = max
            max = c
    a = [0]*n
    for i in range(0,len(a)):
        r=random.randint(min,max)
        for r in a:
            r=random.randint(min,max)
            if r not in a:
                break
        a[i] = r
    return(a)
