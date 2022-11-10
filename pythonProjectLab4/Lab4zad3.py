a = []
b = int(input("Podaj liczbę zwierząt: "))
for i in range(b):
    x = input("Podaj różne zwierzęta")
    a.append(x)
print(a)
a.sort()
print(a)
print(a[-3: ],len(a) )
