def oszlopvissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])

    return oszlop



def oszlopvissza2(hanyadik):
    oszlop=[e[hanyadik-1::hanyadik] for e in tabla]
    return oszlop
   
    
 



print("!számok generálása üres listába!")
tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)   
print(tabla)

print("!első sor kiíratása!")
oszlop=[ ]
for e in tabla:
    #print(e)
    oszlop.append(e[0])
print(oszlop)
print(oszlopvissza(5))
print(oszlopvissza(10))


oszlop=[e[:3] for e in tabla]
oszlop=[e[4:7] for e in tabla]
oszlop=[e[1::2] for e in tabla]
oszlop=[e[3::4] for e in tabla]
print(oszlop)

#print(oszlopvissza2(int(input("Kérek egy számot: "))))

oszlop=[[e[2],e[6],e[0]] for e in tabla]
print(oszlop)









