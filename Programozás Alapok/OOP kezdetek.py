import copy

class MyClass:
    x=5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel


class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def  __init__(self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szin=szin


    def ugat(self):
        print("Vau-vau")

    def koszon(self):
        print("Vau-vau, {} vagyok!".format(self.nev))


        

k1=kutya("Bodri","Puli",3,9,"fekete")
k2=kutya("Morzsi","Golden Retriver",1,3,"világosbarna")

k1.ugat()
k1.koszon()
k2.koszon()

print(MyClass.x)

p1=MyClass()
print(p1.x)
p2=MyClass()
p2.x=1
print(p2.x)

p1.megnovel()
p1.megnovel(10)
print(p1.x)

