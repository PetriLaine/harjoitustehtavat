vuosi = int(input('Syötä vuosiluku '))
if ((vuosi % 4 == 0) & (vuosi % 100 != 0))|(vuosi % 400 == 0):
    print('Vuosi on karkausvuosi')
