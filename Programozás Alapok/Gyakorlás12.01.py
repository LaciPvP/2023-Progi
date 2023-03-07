def oszlopba(munkalista,db):
        for i in range(len(munkalista)):
            print(munkalista[i],end=" ")
        if i%db==db-1:
                print()

             print()
    




lista=[]

for i in range(0):
        lista.append(int(input("Kérek random 10 számot:")))

lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)

for i in range(len(lista)):
    print(lista[i],end=" ")
    if i%3==2:
        print()

print()

keres=int(input("Adj meg egy számot:"))
if keres in lista:
    print("van benne")

else:
    print("nincs benne")


oszlopba(lista,5)







    





