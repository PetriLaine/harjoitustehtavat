tunnus="python"
salasana="rules"
i=0
while i<5:
    tunnusInput=input('Syötä käyttäjätunnus')
    salasanaInput = input('Syötä salasana')
    if (tunnusInput==tunnus)&(salasanaInput==salasana):
        break
    i+=1

if i==5:
    print('Pääsy evätty')
else:
    print('Tervetuloa')


