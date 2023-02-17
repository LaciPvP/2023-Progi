import haromszog

def ujabb(darab=3):
    haromszogek=[ ]
    for i in range(darab):
        haromszogek.append(haromszog.haromszog())

    for e in haromszogek:
        print("\ta={}, b={}, c={}".format(e[0],e[1],e[2]))
        






#lista=haromszog.haromszog()
ujabb()


    



