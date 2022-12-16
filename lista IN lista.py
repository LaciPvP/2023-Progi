import random
#167
#1666
#hattal oszthato, de 12-vel (2*6)nemnagyon

       
print(random.randrange(167,1667,2)*6)

print((random.randint(83,832)*2+1)  *  6)


szavak=["alma","körte","barack","sárkánygyümölcs","dinnye","szölő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

#[ ["alma",14],["körte",18],[ ]...]
print("--------------------------------")
nagyLista=[]
for e in szavak:
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    #print(kisLista)
    nagyLista.append(kisLista)

print(nagyLista)

for e in nagyLista:
    print(e[0].ljust(20),str(e[1]).rjust(4),"kg","*"*(e[1]//10))





#3 jegyu szam bekeres
szamok=int(input("Kérek egy hárm jegyű számot:"))

print(szamok)
    
