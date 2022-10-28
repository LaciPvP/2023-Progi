import math

#a*x2+b*x+c

a = int (input("a="))
b = int (input("b="))
c = int (input("c="))

#(-b+-gyök(b2-4ac)) / 2a

#print (math.sqrt (3))
diszkriminans=b*b-4*a*c
if diszkriminans<0:
    print("nincs megoldas"
)
elif diszkriminans==0:
   megoldas=-b /(2*a)
   print ("egy megoldas van ami a(z): {}".format(megoldas))
else:
    x1= -b+math.sqrt(diszkriminans) / (2*a)
    x2= -b-math.sqrt(diszkriminans) / (2*a)

#gyok=math.sqrt(b*b-4*a*c)
#print (gyok)



