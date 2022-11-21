numerot=[]
luku=input('Syötä lukuja')

while luku!='':
    numerot.append(float(luku))
    luku=input()

numerot.sort(reverse=True)

for i in range(min(5,len(numerot))):
    print(numerot[i])
