import random

def getNun(num):
    if num == 1:
        return 'Num is 1'
    elif num == 2:
        return 'Num is 2'
    elif num == 3:
        return 'Num is 3'
    elif num == 4:
        return 'Num is 4'
    elif num == 5:
        return 'Num is 5'
    elif num == 6:
        return 'Num is 6'
r = random.randint(1, 6 )
f = getNun(r)
print(f)

