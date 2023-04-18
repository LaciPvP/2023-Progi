import copy

#BMW
class auto1:
    marka,szin,tipus,ajtokszam["","","",0]
    def __init__(self,marka,szin,tipus,ajtoszam):
        self.marka=marka
        self.szin=szin
        self.tipus=tipus
        self.ajtoszam=ajtoszam

    def indulas1(self):
        print("Brrrr")

    def duda1(self):
        print("Tutuuuu")

    def iranyjelzo1(self):
        print("Kat-kat-kat")

#AUDI
class auto2:
    marka,szin,tipus,ajtokszam["","","",0]
    def __init__(self,marka,szin,tipus,ajtoszam):
        self.marka=marka
        self.szin=szin
        self.tipus=tipus
        self.ajtoszam=ajtoszam

    def indulas2(self):
        print("Wrooom")

    def duda2(self):
        print("Bííííííp")

    def iranyjelzo2(self):
        print("Kat-kat-kat")

#Mercedes
class auto2:
    marka,szin,tipus,ajtokszam["","","",0]
    def __init__(self,marka,szin,tipus,ajtoszam):
        self.marka=marka
        self.szin=szin
        self.tipus=tipus
        self.ajtoszam=ajtoszam

    def indulas3(self):
        print("vUTUTUTUTU")

    def duda3(self):
        print("CSIRIP CSIRIP")

    def iranyjelzo3(self):
        print("Kat-kat-kat")


Y=input("Kérek egy autó számot: ")
if Y=="auto1":
    print(auto1)
elif Y=="auto2":
    print(auto2)
else:
    print(auto3)



    
