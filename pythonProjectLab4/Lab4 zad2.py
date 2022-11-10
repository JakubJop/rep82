zestaw_1 = []
a = int(input("Podaj liczbę: "))
import random
zestaw_1= [random.randint(1,10)for f in range (a)]
print(zestaw_1)
a = int(input("Podaj liczbę: "))
zestaw_2 = [random.randint(5,15)for g in range(a)]
print(zestaw_2)
l = int(input("Podaj liczbę: "))
if a in (zestaw_1 and zestaw_2):
    print('Liczba jest w obu listach')
elif a in zestaw_1:
    print('Liczba z zestawu 1')
elif a in zestaw_2:
    print('Liczba z zestawu')
else:
    print('Nie ma takiej liczby w obu zestawach')
zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)
zestaw_1_2.sort()
print(zestaw_1_2)
