import Matekmodul
class Teglalap:
    def __init__(self,hossz,szel):
        self.hossz=hossz
        self.szel=szel

    def kerulet(self):
        return 2*(self.hossz+self.szel)

    def terulet(self):
        return self.hossz*self.szel


for i in range(5):
    elso=int(input("Kérem az első számot:"))
    masodik=int(input("Kérem a második számot:"))

Teglalap2=Teglalap(elso,masodik)
kerulet2=Teglalap2.kerulet()
print("A téglalap kerülete: {0}".format(kerulet2))



