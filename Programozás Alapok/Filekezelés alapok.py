gyumolcsok=["alma","körte","banán","barac","cseresznye","paradicsom","eper","licsi"]
print("Ennyi gyümölcs van a gyümölcsök listában: {0}".format(len(gyumolcsok)))

#A 3. elemhez hozzárendeltünk egy ,,K" betűt.
gyumolcsok[3]+="k"
print(gyumolcsok[3])

for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<5:
        print(gyumolcsok)
        
        
    
       








