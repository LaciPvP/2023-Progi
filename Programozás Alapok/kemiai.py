print("1. Feladat")
f=open("felfedezesek.csv")
elemek=[]
for e in f:
    elemek.append((e.replace("\n","").split(";")))
    
f.close()

print(elemek[0])
elemek.pop(0)
print(elemek[0])

    
print("2. Feladat")
print("Elemek száma ennyi: {0}".format(len(elemek)))

print("3. Feladat")
okor=[e for e in elemek if e[0]=="Ókor"]


print("4. Feladat---Felfedezések száma az ókorban ennyi: {0}".format(len(okor)))

print("5. Feladat")
print("a">"b")
while True:
    vegyjel=str(input("Kérek egy vegyjelet: ")).lower()
    if len(vegyjel)<3 and len(vegyjel)>0:
        jo=True
        for i in range(len(vegyjel)):
             if not(vegyjel[i]>="a" and vegyjel[i]<="z"):
                 jo=False

        if jo:
            break

 #print(vegyjel)

print("6. Feladat")
keresett=[e for e in elemek if e[2].lower()==vegyjel]
if keresett==[]:
    print("Nincs ilyen elem az adatforrásban!")
print(keresett)
    
                
        

