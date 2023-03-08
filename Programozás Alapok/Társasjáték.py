from random import randint
jelek=["Kavics","Papír","Olló"]
t = ["Kavics", "Papír", "Olló"]

gep = t[randint(0,2)]

jatekos = False

while jatekos == False:
    jatekos = input("Válassz egyet: Kő/Papír/Olló<---->")
    if jatekos == gep:
        print("Döntetlen!")
    elif jatekos == "Kavics":
        if gep == "Papír":
            print("Vesztettél!", gep, "becsomagolta őt: ", jatekos)
        else:
            print("Nyertél!", jatekos, "lezúzta őt: ", gep)
    elif jatekos == "Papír":
        if gep == "Olló":
            print("Vesztettél...", gep, "szétkaszabolta őt: ", jatekos)
        else:
            print("Nyertél!", jatekos, "kicsorbította őt: : ", gep)
    elif jatekos == "Olló":
        if gep == "Kő":
            print("Vesztettél...", gep, "kicsorbította őt: : ", jatekos)
        else:
            print("Nyertél!", jatekos, "szétkaszabolta őt: ", gep)
    else:
        print("Ez nem egy játékban használt kézjel,válassz az alábbiak közül: {0}".format(jelek))
    jatekos = False
    gep = t[randint(0,2)]
