print("1. Feladat")
szoveg=input("Kérek egy szöveget: ")
szam=""
while type(szam)!=int:
    try:
        szam=int(input("Kérek egy egész számot: "))
    except:
        print("Ez nem egész szám!! ")

try:
    print(szoveg[szam-1]*szam)
except:
    print("Nincs ilyen betű")


