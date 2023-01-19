import random
#Függvény,ami bekér egy szót + leírás(jelentés)

def szoBeker():
    szo=input("Kérek egy szót:")
    if szo =="":
        jelentes=""
    else:
        jelentes=input(szo+" ""jelentése:")
    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()
    return szavak


     
print(sokBeker())    
