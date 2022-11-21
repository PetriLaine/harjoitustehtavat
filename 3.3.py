sukupuoli = input('Syötä biologinen sukupuolesi ')
arvo = int(input('Syötä hemoglobiiniarvo (g/l) '))
if sukupuoli == 'mies':
    if arvo < 134:
        print('Hemoglobiiniarvo on alhainen')
    elif arvo > 195:
        print('Hemoglobiiniarvo on korkea')
    else:
        print('Hemoglobiiniarvo on normaali')
elif sukupuoli == 'nainen':
    if arvo < 117:
        print('Hemoglobiiniarvo on alhainen')
    elif arvo > 175:
        print('Hemoglobiiniarvo on korkea')
    else:
        print('Hemoglobiiniarvo on normaali')