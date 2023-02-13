def pontSzamit(valasz,helyes):
    pont=0
    for sorszam,betu in enumerate(valasz):
        if betu == helyes[sorszam]:
            if sorszam < 5:
                 pont+=3
            elif sorszam < 10:
                pont += 4
            elif sorszam < 14:
                pont+=5
            else:
                pont+=6
    return pont 
 
        

f=open("valaszok.txt")

adatok=f.read().split("\n")
#1. megoldás
adatok.remove("")
#2.megoldás
#adatok=adatok[:-1]

f.close()

#print(adatok)

helyes=adatok[0]
adatok.remove(helyes)

valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))


#print(valaszok)    


print("2.Feladat A vetélkedőn " + str(len(valaszok)) + " versenyző indult.")


versenyzo = input("3. feladat: A versenyző azonosítója = ")

versenyzoValasza=""
for e in valaszok:
    if e[0] == versenyzo:
       versenyzoValasza=e[1]

                
print("{}\t(a versenyző válasza)".format([e[1] for e in valaszok if e[0] == versenyzo][0]))


print("4. feladat")
print(helyes + "\t(a helyes megoldás)")
print(versenyzoValasza)


for sorszam,betu in enumerate(versenyzoValasza):
    #print(betu)
    if betu == helyes[sorszam]:
        print("+", end="")

    else:
        print(" ", end="")

print("\t (A versenyző helyes válaszai)")

feladat=int(input("5.Feladat: a Feladat sorszáma= "))

db=0

for e in valaszok:
    if e[1][feladat] == helyes[feladat]:
        db+=1


print("A feladatra {0} fő, a versenyzők {1:.2%}-a adott helyes választ.".format(db,db/len(valaszok)))
    

f=open("pontok.txt","w")
for e in valaszok:
    pont=pontSzamit(e[1],helyes)
    f.write(e[0]+" "+str(pont)+"\n")


f.close()

