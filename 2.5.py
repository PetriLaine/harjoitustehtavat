massa=8512*float(input('Anna leiviskät. '))
massa+=425.6*float(input('Anna naulat. '))
massa+=13.3*float(input('Anna luodit. '))
print('Massa nykymittojen mukaan: '+str(int(massa/1000))+' kilogrammaa ja '+str(float(massa%1000))+' grammaa.')
