szamok=[]
for i in range(10):
    szamok.append(int(input(str(i+1)+". szam:")))

for i in szamok:
    print(str(i),end="")
print()
print("vége")

#print("".join(szamok))

for i in range (10):
    print(str(i)+"\t",end="")
    if  i%3==2:
     print()

print()


atlag=sum(szamok)/len (szamok)
print(atlag)

osszeg=0

for i in szamok:
    osszeg+=i
atlag=osszeg/len(szamok)

szoveg="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."
betu="qwe"
while betu !="":
    betu=input("Kérek egy betűt:")
    szoveg=szoveg.replace(betu,betu.upper())
    print(szoveg)

lista=szoveg.split(" ")
lista.reverse()
szoveg2"".join(lista)
print(szoveg2)




    
