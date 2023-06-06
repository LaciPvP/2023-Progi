class szavak:
    def __init__(self,szavak):
        self.szavak=szavak
    def minta(self,szo):
        vissza=""
        for i in range(6):
            if szo[i]==self.szavak[i]:
                vissza+=szo[i]
            else:
                vissza+="."

        return vissza
