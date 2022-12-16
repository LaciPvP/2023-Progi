
szamok="12"
while len(szamok) !=3:
        szamok=input("Kérek egy háromjegyű szám:")



szamok=int(szamok)

if szamok%12==0:
    print("!!Osztható!!")
elif szamok%12!=0:
    print("!!Nem Osztható!!")

print(szamok)


