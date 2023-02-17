def haromszog():
        for i in range(3):
            szam=""
            while type(szam)!=int:
                try:
                    szam=int(input("Kérek egy egész számot: "))
                except:
                    print("Ez nem egész szám!! ")
