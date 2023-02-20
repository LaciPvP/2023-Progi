
def ido2mp():
    pass
    





# 1.Feladat 
eredmenyek=[]
f=open("triatlon.txt")

for sor in f:
    temp=sor.replace("\n","").split(";")
    eredmenyek.append(temp)
    







f.close()

eredmenyek.pop(0)
print(eredmenyek)

# 2.Feladat
print("2.Feladat")
print("A versenyen {0} versenyző indult".format(len(eredmenyek)))

# 3.Feladat
print("3.Feladat")

   
    
