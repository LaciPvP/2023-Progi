import modulka

f=open("szavak.txt")
sorok=[]
for e in f:
    sorok.append(e.split())
    


f.close()
print(sorok)
