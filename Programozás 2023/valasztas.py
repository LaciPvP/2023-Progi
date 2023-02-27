f=open("szavazatok.txt")
tarolas=[]
for e in f:
        tarolas.append(e.replace("\n","").split(" "))
f.close()
print(tarolas)

print("2. Feladat")
print("A helyhatósági választáson {0} jelölt indult".format(len(tarolas)))

print("3. Feladat")
neve1=(input("Írd be a vezetéknevet:"))
neve2=(input("Írd be a keresztnevet:"))
nevek=[]
hiba=("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban")

for e in tarolas:
    if e[2]==neve1 and e[3]==neve2:
        nevek.append(e)
print(nevek)
print(len(nevek))

print("4. Feladat")





    















    
