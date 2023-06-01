print("1.Feladat")
beKer=input("Kérek egy szöveget:")

string=""

while type(string)!=int:
    try:
        beKer2=int(input("Kérek egy egész számot:"))
        break
    except:
        print("Ez nem egy egész szám!")

try:
    print(beKer[string-1]*beKer)
except:
    print("Sajnos nincs ilyen betű!")

