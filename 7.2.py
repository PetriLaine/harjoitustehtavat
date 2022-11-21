nimi=' '
nimet={""}

while nimi!='':
    nimi=input('Syötä nimi ' )
    if nimet.__contains__(nimi):
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        nimet.add(nimi)
