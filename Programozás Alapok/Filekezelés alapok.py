gyumolcsok=["alma","körte","banán","barac","cseresznye","paradicsom","eper","licsi"]
print("Ennyi gyümölcs van a gyümölcsök listában: {0}".format(len(gyumolcsok)))

#A 3. elemhez hozzárendeltünk egy ,,K" betűt.
gyumolcsok[3]+="k"
print(gyumolcsok[3])


rovid=[]
print("Rövid nevű gyümölcsök:")
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
print("1. Megoldás")        
print(rovid )
print("-"*50)
rovid=[]
for e in gyumolcsok:
    if len(e)<5:
        rovid.append(e)
print("2. Megoldás")
print(rovid)
print("-"*50)
rovid=[e for e in gyumolcsok if len(e)<5]
print("3. Megoldás")
print(rovid)
print("-"*50)
rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    i+=1
print("4. Megoldás")
print(rovid)
print("-"*50)
i=0
rovid=[]
while True:
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    if len(gyumolcsok)-1==i:
        break
    i+=1
print("5. Megoldás")
print(rovid)
print("-"*50)
print("Lista tagolás")
print(gyumolcsok[:2])

print(gyumolcsok[-2:])
print(gyumolcsok[len(gyumolcsok)-2:])
print(gyumolcsok[1:-1])
print("-"*50)
paratlan=gyumolcsok[1::2]
print("Ezek a páratlan gyümölcsök: {0}".format(paratlan))
paros=gyumolcsok[::2]
print("Ezek a páros gyümölcsök: {0}".format(paros))

print("Fordított kiíratás")
masolat=gyumolcsok
masolat.reverse()
print(masolat)
print("-"*50)
print("Fordított kiíratás #2")
masolat=gyumolcsok
print(masolat[::-1])









  
    
       








