#Filekezelés

f=open("proba.txt","w")
f.write("helló")
f.write("\n")
f.write("világ")

f.close()

<<<<<<< HEAD
#file tartalma soronként 1
f=open("proba.txt","r")
szoveg=f.read()
=======

f=open("proba.txt","r")

szoveg=f.read()
print(f.readline())

>>>>>>> d269ad6d21bf02c642aa3dff74b9ed8069bb7870
sorok=szoveg.split("\n")
print(sorok)

f.close()

<<<<<<< HEAD

#file tartalma soronként 2
=======
>>>>>>> d269ad6d21bf02c642aa3dff74b9ed8069bb7870
f=open("proba.txt","r")
sorok=[]
for sor in f:
    sorok.append(sor.replace("\n"," ").replace("\r"," "))
    

print(sorok)
f.close()
