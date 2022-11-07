import matplotlib.pyplot as plt


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
plt.show()
