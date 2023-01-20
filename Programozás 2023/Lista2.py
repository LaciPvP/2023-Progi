szavak=["ló","bakfitty","csutora",]
számok=[1,0,3000,2]


print(szavak)
szavak.sort() 
print(szavak)
szavak.append("hát")
print(szavak)
szavak.sort()
print(szavak)
szavak.insert(1,"az hogy")
print(szavak)
darab=számok.count(20)
print(darab)
számok.append(20)
számok.append(20)
darab=számok.count(20)
print(darab)
számok.remove(20)
print(számok)
for szam in számok:
    print("szám:"+str(szam))
