import random

def find(lista2, wartość):
    lista2 = []
    for x in range(0,len(lista)):
        if lista[x]==wartość:
            lista2.append(x)



lista = [random.randint(0, 10) for x in range (10)]
print(lista)
userIn= int(input("Podaj szukaną wartość: "))
print(find(lista, userIn))


