import random
pisteet=int(input('Syötä arvottavien pisteiden määrä'))
osuma=0
i=0
while i<pisteet:
    x=random.uniform(-1.0,1.0)
    y = random.uniform(-1.0, 1.0)
    if x*x+y*y<1:
        osuma+=1
    i+=1
print(str(4*osuma/pisteet))