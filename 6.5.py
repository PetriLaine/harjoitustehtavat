def parilliset(lista):
    for x in lista:
        if x%2!=0:
            lista.remove(x)
    return lista

lista=[2,4,5,6,7,8,9,10]
print(lista)
print(parilliset(lista))
