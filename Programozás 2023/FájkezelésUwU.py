import random

# ez a függvény bekér egy szót, és annak jelentését.
#visszaad: a két bekérés listában
def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo== "":
        jelentes=""
    else:
        
        jelentes=input(szo + " jelentése: ")
    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()


    return szavak

def filebaIr(lista):
    f=open("szotar.txt","a")
    for e in lista:
        
        #print(e)
        f.write(" ".join(e))
        f.write("\n")
        
    f.close()


kerdesek=[]
def beolvas():
    f=open("szotar.txt","r")
    for sor in f:
        #apple alma
        kerdesek.append(sor.replace("\n","").split(" "))
        
    f.close() 
    
def kerdez():
    #jó válasz
    valasztott=random.choice(kerdesek)
    print("valasztott:",  valasztott)
    #rossz válaszok 3db
    rossz=[ ]
    for i in range(3):
        temp=random.choice(kerdesek)
       # print("temp",temp)
        #ez teljesen rossz
        while not(temp not  in rossz and temp != valasztott):
            temp=random.choice(kerdesek)
            
        rossz.append(temp)
        print("rossz",rossz)
        
    print("-"*40)
    print("Mit jelent: " + valasztott[0] + "?")

    rossz.append(valasztott)
    print(rossz)
                

    #válasz bekérés
    abc="abcdefghijklmnopqrstuvxyz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+": :"+e[1])
        i+=1

    valasz=input("Válassz :  ")
    hol=abc.index(valasz)
    print(hol)
    while hol>=4:
        try:
            valasz=input("Válassz újra")
            hol=abc.index(valasz)
        except(e):
            pass
        
        
    
    

beolvas()
kerdez()
#szavak=sokBeker()
#filebaIr(szavak)
