luku=int(input('Syötä luku'))

alkuluku=True
for i in range(luku-1,1,-1):
    if luku%i==0:
        alkuluku=False
        break

if alkuluku:
    print(f'{luku} on alkuluku')
else:
    print(f'{luku} ei ole alkuluku')
