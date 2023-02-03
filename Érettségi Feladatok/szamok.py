import random

f=open("felszam.txt","r")

kerdesek=[ ]
for sor in f:
    josor=sor.replace("\n","")
    josor2=f.readline().replace("\n","")
    temp=josor2.split(" ")

    kerdesek.append([josor,int(temp[0]),int(temp[1]),temp[2]])

f.close()

print("2. feladat: ")
print("Az adatflile-ban: "+str(len(kerdesek)) +" kérdés van.")

matek=[ ]
for e in kerdesek:
    if e [3]=="matematika":
        matek.append(e[2])

print("Az adatfájlban " + str(len(matek)) + "  matematika feladat van, 1 pontot er "+ str(matek.count(1)) +" feladat, 2 pontot er "+str(matek.count(2))+ " feladat, 3 pontot er " +str(matek.count(3))+" feladat. ")





valaszok=[ ]
for e in kerdesek:
    valaszok.append(e[1])


valaszok=[e[1] for e in kerdesek]
print("A válaszok számértéke {}-től {}-ig tart.".format(min(valaszok),max(valaszok)))


temakorok=[ ]
for e in kerdesek:
    if e[3] not in temakorok:
        temakorok.append(e[3])

print("5. feladat")
print("A témakörök: "+", ".join(temakorok))


print("6. feladat")
beker=input("Milyen témakörből szeretne kérdést kapni? ")
ujLista=[e for e in kerdesek if e [3]==beker]

sorsolt=random.choice(ujLista)

valasz=input(sorsolt[0])
if int(valasz)==sorsolt[1]:
    print(str(sorsolt[2])+" pont")
else:
    print("0 pont")
    print("A helyes válasz: "+str(sorsolt[1]))


lista10=[]
for i in range(10):
        r=random.choice(kerdesek)
        while r in lista10:
                r=random.choice(kerdesek)

        lista10.append(r)

print(lista10)

#megkeveri és kiírajta a listát
random.shuffle(kerdesek)
lista10=kerdesek[0:10]

print(len(lista10))

f=open("tesztfel.txt","w")

ossz=0
for e in lista10:
        f.write(str(e[2])+" "+str(e[1])+" "+e[0]+"\n")
        ossz+=e[2]

         
f.write("A feladatsorban összesen {0} pont adható.".format(ossz))
f.close()
                















