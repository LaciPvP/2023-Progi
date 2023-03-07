animals=("bence","martin","giraffe","kelgyó","kágyilló")
print(animals[1])
print(animals[-1])
print(animals[:3])
print(animals[1:-1])

animals=list(animals)
animals[1]="milán"
animals=tuple(animals)
print(animals[1])

ures=[]
print(ures)
for i in range (4,-1,-1) :
    print(i)
    ures.append(animals[i])

print(ures)

