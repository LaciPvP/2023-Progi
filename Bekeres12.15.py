import random

minimumErtek=int(input("Add meg, hogy hol kezdődjön:"))
maximumErtek=int(input("Add meg, a maximum értéket:"))
darab=int(input("Add meg, hány darabot jelenítsek meg:"))

lista=[]

for i in range(darab):
    lista.append(random.randint(minimumErtek,maximumErtek))

print(lista)

for e in lista:
    print(e,"-"*(e[1]//10))
