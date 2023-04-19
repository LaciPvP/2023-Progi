# Import the required libraries
from tkinter import *
import math

#---------------------------
def eltol(pontok, x, y):
    vissza = []
    for e, pont in enumerate(pontok):
        if e % 2 == 0:
            vissza.append(pont + x)
        else:
            vissza.append(pont + y)
    return vissza

#-----------------------------
def nagyit(pontok, meret = 1):
    vissza = []
    for e in pontok:
            vissza.append(e * meret)
    return vissza

#-----------------------------
def forgat(pontok, szog):
    vissza = []
    for i, pont in enumerate(pontok):
        if i % 2 == 0:
            szogRadian=math.radians(szog)
            
            x = pontok[i]*math.cos(szogRadian) - pontok[i+1]*math.sin(szogRadian)
            y = pontok[i]*math.sin(szogRadian) + pontok[i+1]*math.cos(szogRadian)
            vissza.append(x)
            vissza.append(y)
    return vissza

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("900x900")

# Create a canvas widget
canvas=Canvas(win, width=900, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
A1 = [180,170,200,170,220,130,300,130,320,170,340,170,270,10,250,10,180,170]
A2 = [230,110,290,110,260,30,230,110]
T = [350,10,510,10,510,30,440,30,440,170,420,170,420,30,350,30,350,10]
Y = [520,10,540,10,610,70,680,10,700,10,620,82,620,170,600,170,600,82,520,10]
I = [710,10,730,10,730,170,710,170,710,10]

MATYI = [#M
        [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10],
        #A
        [180,170,200,170,220,130,300,130,320,170,340,170,270,10,250,10,180,170],
        [230,110,290,110,260,30,230,110],
        #T
        [350,10,510,10,510,30,440,30,440,170,420,170,420,30,350,30,350,10],
        #Y
        [520,10,540,10,610,70,680,10,700,10,620,82,620,170,600,170,600,82,520,10],
        #I
        [710,10,730,10,730,170,710,170,710,10]]


for i,betu in enumerate(MATYI):
    betu+=betu[:2]
    betu=nagyit(betu,0.7)
    betu=eltol(betu,200,200)


kozep=[0,0]
db=0
for betu in MATYI:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)
kozep[0]/=db
kozep[1]/=db
    
    

for betu in MATYI:
    betu=eltol(betu,-kozep[0],-kozep[1])
    betu=forgat(betu,90)
    betu=eltol(betu,kozep[0],kozep[1])
    canvas.create_line(betu, fill="black", width=5)
    

win.mainloop()
