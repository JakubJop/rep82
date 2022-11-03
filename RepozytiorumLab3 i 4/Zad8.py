x=int(input("Podaj ilość wierszy: "))
y=int(input("Podaj ilość kolumn: "))
for i in range(0,y):
 for j in range(x):
        print( *"*", end=" ")
        print()