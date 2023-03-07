print("1. Feladat")
f=open("jarmu.txt")
gepek=[]
for e in f:
    gepek.append(e.replace("\n","").split(" "))
f.close()
print(gepek)
    



   
("2. Feladat")






print("3. Feladat")

for e in munkaido:
    if e[0]==str(10):
        print(e[0]+[1]+[2]+"Óra:"+e[3])

       
print("4. Feladat")
B=["Autóbusz"]
K=["Kamion"]
M=["Motor"]
       
for e in munkaido:
    if e[3]==(B):
        print(B)
       
    elif e[3]==K:
        print(K)

    elif e[3]==M:
        print(M)

print("5. Feladat")   
