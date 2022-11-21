luku=input('Syötä lukuja. Tyhjä merkkijono lopettaa')
pienin=float(luku)
suurin=float(luku)
while luku != '':
    if float(luku) < pienin:
        pienin = float(luku)
    if float(luku) > suurin:
        suurin = float(luku)
    luku=input()
print(f'Pienin luku oli {pienin} ja suurin luku oli {suurin}')
