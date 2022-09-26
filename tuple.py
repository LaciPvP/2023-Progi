animals=("bence","martin","giraffe","kelgyó","kágyilló")
print(animals[1])
print(animals[-1])
print(animals[:3])
print(animals[1:-1])

animals=list(animals)
animals[1]="milán"
animals=tuple(animals)
print(animals[1])

