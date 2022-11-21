import math

def hinta(hinta,halkaisija):
    return hinta/(math.pi*(halkaisija/2)*(halkaisija/2))

hinta1=hinta(float(input('Syötä ensimmäisen pizzan hinta ')),float(input('Syötä ensimmäisen pizzan halkaisija ')))
hinta2=hinta(float(input('Syötä toisen pizzan hinta ')),float(input('Syötä toisen pizzan halkaisija ')))

if hinta1<hinta2:
    print(f'Ensimmäinen pizza on edullisempi, {hinta1}€/cm^2')
else:
    print(f'Toinen pizza on edullisempi, {hinta2}€/cm^2')