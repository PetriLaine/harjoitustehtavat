lentokentät={}
o=0
while o!=3:
    o=int(input('Valitse operaatio\n1 Lisää uusi lentoasema\n2 Hae lentoasemaa\n3 Lopeta '))
    if o==1:
        lentokentät[input('Syötä kentän ICAO koodi ')]=input('Syötä kentän nimi ')
    elif o==2:
        print(lentokentät[input('Syötä ICAO koodi ')])