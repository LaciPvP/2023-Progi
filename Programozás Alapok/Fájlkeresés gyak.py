import random
import math

napok=[31,28,31,30,31,30,31,31,30,31,30,31]

f=open("Datumok.txt","w")


for i in range(100):
    ev=random.randint(2003,2008)
    honap=random.randint(1,12)
    nap=random.randint(1,napok[honap-1])
    datum=(str(ev)+"."+str(honap)+"."+str(nap))
    print(datum)
    f.write(datum)
    f.write("\n\r\r\n")

f.close()


def uj()

    
    

