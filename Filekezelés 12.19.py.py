#Filekezelés

f=open("proba.txt","w")
f.write("helló")
f.write("\n")
f.write("világ")

f.close()

#file tartalma soronként 1
f=open("proba.txt","r")
szoveg=f.read()
sorok=szoveg.split("\n")
print(sorok)

f.close()


#file tartalma soronként 2
f=open("proba.txt","r")
sorok=[]
for sor in f:
    sorok.append(sor.replace("\n"," ").replace("\r"," "))
    

print(sorok)
f.close()
