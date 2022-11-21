import random

def noppa(tahkot):
    return random.randint(1,tahkot)

tahkot=int(input('Syötä tahkojen lukumäärä '))
i=0
while i!=tahkot:
    i=noppa(tahkot)
    print(i)