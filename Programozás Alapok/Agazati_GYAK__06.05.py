import random
import modulka

f=open("szavak.txt")
l=[]
for e in f:
    l.append(e.replace("\"",'').strip())

f.close()
#--------------------------------
sorok=l[0].split(", ")

szavak=[]
for e in sorok:
    szavak.append(modulka.szavak(e))

print(szavak)

print("2.Feladat")
rejtett=random.choice(szavak)
print(rejtett.szavak)
#--------------------------------
print("3.Feladat")
tippek=[]
while True:
    be=input("Kérek egy szót(min/max 6 betű): ")
    tippek.append(be)
    
    if be=="stop":
        break

    vissza=rejtett.minta(be)
    
    print("Az eredmény: {}".format(vissza))
    if vissza==be:
        break

if tippek[-1]=="stop":
    pass
else:
    print("{} tippeléssel sikerült kitalálni.".format(len(tippek)))    

        
    
