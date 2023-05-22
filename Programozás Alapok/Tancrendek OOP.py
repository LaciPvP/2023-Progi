class tanc:
    def __init__(self,tanc,lany,fiu):
        self.tanc=tanc
        self.lany=lany
        self.fiu=fiu

    def __str__(self):
        return "tanc: {}, lány: {}, fiú: {}".format(self.tanc,self.lany,self.fiu)

    def isVilma(self):
        return self.lany=="Vilma"
       


f=open("tancrendecske.txt")

sorok=[]
#2. megoldas
tancok2=[]
temp=[]
for e in f:
    sorok.append(e.strip())
    #2. megoldas
    if len(temp)<3:
        temp.append(e)
    else:
        tancok2.append(tanc(temp[0],temp[1],temp[2]))

f.close()
print(sorok)
print(sorok[:3])

#1. megoldas
tancok=[]
for i in range(len(sorok)//3):
    tancnev=sorok[i*3]
    lany=sorok[i*3+1]
    fiu=sorok[i*3+2]
    tancok.append(tanc(tancnev,lany,fiu))
   


#hazi:ezen a megoldason kivul mas fajta megoldas is es az elso aki bekuldi az kapja

print("2. feladat")
print("Első tánc: {0},Útolsó tánc: {0}".format(tancok[0].tanc,tancok[-1].tanc))

db=0

for egytanc in tancok:
    if egytanc.tanc=="samba":
        db+=1
print("Ennyi samba volt: {}".format(db))

print("Vilma ezekben szerepelt: ")

for egytanc in tancok:
    if egytanc.isVilma():
        print(egytanc.tanc)


tancNev=input("Kérek egy táncnevet:")
for elem in tancok:
    #print(elem)
    if elem.lany=="Vilma" and elem.tanc==tancNev:
        print("A {} bemutatóján Vilma párja {} volt".format(tancNev,elem.fiu))
        break
else:
    print("Vilma nem táncolt {}-t".format(tancNev))

fiu=[]
lany=[]

for egyTanc in tancok:
    if egyTanc.fiu not in fiu:
        fiu.append(egyTanc.fiu)

for egyTanc in tancok:
    if egyTanc.lany not in lany:
        lany.append(egyTanc.lany)

print(", ".join(fiu))
print(", ".join(lany))


f=open("szereplok.txt","w")
f.write("Lányok: "+" ".join(lany)+"\n")
f.write("Fiúk: "+" ".join(lany)+"\n")


f.close()

statFiu={}
for egy in fiu:
    statFiu[egy]=0

print(statFiu)
    



    
    


  
