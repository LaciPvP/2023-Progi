#1. feladat
f=open("valaszok.txt")
adatok=f.read().split("\n")
#1.megoldás
#adatok.remove("")
#2.megoldás
adatok=adatok[:-1]



#print(adatok)
f.close()

helyes=adatok[0]
adatok.remove(helyes)
valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))
print(valaszok)

