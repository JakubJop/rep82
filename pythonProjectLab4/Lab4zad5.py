b=15
import random
punkty = []
for i in range(15):
    a = random.uniform(0,50)
    a = round(a,2)
    punkty.append(a)
print(punkty)
print("wartość maksymalna", max(punkty))
print("wartość minimalna", min(punkty))
x = float(input("Podaj liczbę punktów: "))
if b in punkty :
   y = (punkty.index(x))
   print(y)
else:
   print("Wartość nie występuję na liście ")

#Oblicz średnią liczbę punktów z egzaminu

a=sum(punkty)
b=15
print("Średnia: ", round(a/b,2))
# Oblicz ile osób zdobyło punkty poniżej średniej
punkty_2= []
for i in range (b):
    if punkty (i) >sr:
        punkty_2.append(punkty[i])
print(punkty_2)




