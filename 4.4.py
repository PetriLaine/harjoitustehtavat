from random import randint

luku=randint(1, 10)
arvaus=int(input('arvaa luku'))
while arvaus != luku:
    if arvaus < luku:
        print('Liian pieni arvaus')
    if arvaus > luku:
        print('Liian suuri arvaus')
    arvaus = int(input())
print('Oikein')