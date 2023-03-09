from random import randint
jelek=["Kő","Papír","Olló","Kalapács","Deszka","Fűrész"]
t = ["Kő", "Papír", "Olló","Kalapács","Deszka","Fűrész"]
gep = t[randint(0,2)]
#----------------------------------
jatekos = False
print("Kő-Papír-Olló-Kalapács-Deszka-Fűrész")
#---------------------------------
jatekos=0
while jatekos == False:
#Itt vannak azok a lehetőségek ahol a játékos veszít.
    jatekos = input("Válassz egy tárgyat: ")
    if jatekos == gep:
       print("Ugyan azt választottátok,így ez a kör döntetlen!")
    if jatekos =="Kő" and gep=="Papír":
        print("A papír becsomagolja a követ...vesztettél!")
    elif jatekos =="Olló" and gep=="Kő":
        print("A kő kicsorbítja az ollót...vesztettél!")
    elif jatekos =="Papír" and gep=="Olló":
        print("Az olló elvágja a papírt...vesztettél!")
    elif jatekos =="Olló" and gep=="Kalapács":
        print("A kalapács széttöri az ollót...vesztettél!")
    elif jatekos =="Kalapács" and gep=="Papír":
        print("A kalapácsot becsomagolja a papír...vesztettél!")
#Itt vannak azok a lehetőségek ahol a játékos nyer.
    elif jatekos =="Papír" and gep=="Kő":
        print("Nyertél...becsomagoltad őt: {0}!".format(gep))
    elif jatekos =="Kő" and gep=="Olló":
        print("Nyertél...kicsorbítottad őt: {0}!".format(gep))
    elif jatekos =="Olló" and gep=="Papír":
        print("Nyertél...elvágtad őt: {0}!".format(gep))
    elif jatekos =="Kalapács" and gep=="Olló":
        print("Nyertél...széttörted őt: {0}!".format(gep))
    elif jatekos =="Papír" and gep=="Kalapács":
        print("Nyertél...becsomagoltad őt: {0}!".format(gep))
        
        
        
    jatekos = False
    gep = t[randint(0,2)]
