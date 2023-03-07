def ado(adosav,alapterulet):
    alapterulet=int(alapterulet)
    if adosav == "A":
        ar=int(arak[0])*alapterulet
    elif adosav == "B":
        ar=int(arak[1])*alapterulet
    else:
         ar=int(arak[2])*alapterulet

    if ar>=10000:
        return ar
    else:
        return 0 







    
f=open("utcak.txt")
hazak=[]
for e in f:
    hazak.append(e.replace("\n","").split(" "))
    
    

f.close()

arak=hazak.pop(0)
print("2. Feladat A mintában {} telek található".format(len(hazak)))

adoszam=(input("3. Feladat Egy tulajdonos adószáma: "))
cimek=[]
for e in hazak:
    if e[0]==adoszam:
        cimek.append(e)

#A (for e in hazak) és a cimek=[] ugyan az csak 1 sorban
#cimek=[e for e in hazak e[0]==adoszam]

if len(cimek)==0:
    print("Nem szerepel az alany az adóállományban! ")
else:
    for e in cimek:
        print("{} utca {}".format(e[1],e[2]))

#print(ado("C",120))

        
hazakA=[e for e in hazak if e[3]=="A"]

hazakB=[]
for e in hazak:
    if e[3]==adoszam:
        hazakB.append(e)

hazakC=[e for e in hazak if e[3]=="C"]

arak=[]
for i in range(len(hazakA)):
    hazakA[i].append(ado(hazakA[i][3],hazakA[i][4]))

for i in range(len(hazakA)):
    hazakB[i].append(ado(hazakB[i][3],hazakB[i][4]))

for i in range(len(hazakA)):
    hazakC[i].append(ado(hazakC[i][3],hazakC[i][4]))


    




