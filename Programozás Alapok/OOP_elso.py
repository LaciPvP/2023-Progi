class muvelet:
    szam1=0
    szam2=0
    def __init__(self,szam1,szam2):
        self.szam1=szam1
        self.szam2=szam2

    def osszeadas(self):
        return self.szam1+self.szam2

    def kivonas(self):
        return self.szam1-self.szam2

    def szorzas(self):
        return self.szam1*self.szam2

    def osztas(self):
        return self.szam1/self.szam2


#Teszteléshez egy programkód
if True:
#if __name__ == "__main__":
    q=muvelet(10,-10)
    print(q.osszeadas())#0
    print(q.kivonas())#20
    print(q.szorzas())#-100
    print(q.osztas())#-1.0
    




        
    
    

