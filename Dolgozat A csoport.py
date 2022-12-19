#1. Kérj be 8 számot egy megfelelő adatszerkezetbe!
szamok=[]
for i in range(8):
    szamok.append(int(input(str(i+1)+".szam:")))

#2. A bekért számokat írasd ki egymás mellé!
for i in szamok:
    print(str(i),end="")
    
print()
print("vége")

#3. A bekért számokat írasd ki 4 oszlopba!
for i in range(10):
    print(str(i)+"\t",end="")
    if i%4==0:
        print()

#4. Számold ki a bekért számok összegét!
osszeg=sum(szamok)
print("A számok összege:",osszeg)

#5. A mellékelt szöveget tárold el a programodban:
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

#6. Kérj be egy betűt, és írd ki, hogy mennyiszer található meg az előbbi szövegben!
#7. Feladat: Ismételd az előzőt "end" (ez egy szó) végjelig!
vege=""
while vege!="end":
    vege=input("Kérek egy random betűt:")
    szoveg2=szoveg.count(vege)
    print(szoveg2)
    
#8. Feladat: Az eltárolt szöveget írasd ki fordított sorrendben (betűnként)!
print(szoveg[::-1])

#9. feladat: Az eltárolt szövegből töröld az "orna" szöveget! Mekkora most a mérete?
print("A szöveg hossza előtte:",len(szoveg))
print()
szoveg.replace("orna","")
print(szoveg)
print()
print("A szöveg hossza utána:",len(szoveg))

#10. feladat: Készíts egy függvényt, ami bekér 1 karaktert (addig folytatja, amíg 1-et nem kap)! A bekért karakterrel rajzolja ki a következő ábrát:
	#A következő számpárokból készíts egy listát (listák listája) ami alapján készíts egy rajzot!
	#Az első szám a szóközök számát, a második a bekért karakter (kiírandó) darabszámat jelenti 1 sorban.




