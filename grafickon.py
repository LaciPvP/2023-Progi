import matplotlib.pyplot as plt

def fv(a,b,c):
    xPont=[ ] 
    yPont=[ ]

    for x in range(-10,10):
        xPont.append(x)
        yPont.append(a*x**2+b*x+c)

        return(xPont , yPont)

def fv2(*egyutthatok):
    for i in egyutthatok:
        print(i)

import numpy as np

x=[1,10]
y=[10,1]

 
#y =  6x2+ 4x -16
#y = 16x2 -3 +13

xPont=[]
yPont=[]

for x in range(-10,10):
    xPont.append(x)
    yPont.append(6*x**2+ 4*x -16)

plt.plot(xPont,yPont)



xPont=[]
yPont=[]

for x in range(-10,10):
    xPont.append(x)
    yPont.append(16*x**2 -3 +13)

plt.plot(xPont,yPont)

pontok=fv(10,100,1)
plt.plot(pontok[0],pontok[1])

#plt.show()

fv2(1,2,3,4,5,)




