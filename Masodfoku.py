import math

def egyenlet(a,b,c):
      szoveg="0 = "
      if a!=0:
          szoveg+=str(a)+"x²"
       
      if b>0:
          szoveg+=" + "+str(b)+"x"
   
      elif b<0:
          szoveg+=" + "+str(b)+"x"

      if c>0:
          szoveg+=" + "+str(c)
   
      elif c<0:
          szoveg+="  "+str(c)

      return szoveg

def gyokTenyezosSzorzat(a,x1,x2):
      if x1 ==" ":
          return "Nincs gyöktényezős alak."      
          if x1<0:
                return  str (a)+"(x + "+str(-1*x1) +") ²"
          elif x1>0:
                return  str (a)+"(x - "+str(-1*x1) +") ²"
          else:
                return  str (a)+"x²"
      else:
            if x1<0:
                if x2<0:
                    return  str (a)+"(x + "+str(-1*x1) +")(x + "+str(-1*x2) +")"
                elif x2>0:
                    return  str (a)+"(x + "+str(-1*x1) +")(x - "+str(-1*x2) +")"
                else:
                    return  str (a)+"(x + "+str(-1*x1) +")x"
            elif x1>0:
                if x2<0:
                        return  str (a)+"(x - "+str(-1*x1) +")(x + "+str(-1*x2) +")"
                elif x2>0:
                    return  str (a)+"(x - "+str(-1*x1) +")(x - "+str(-1*x2) +")"
                else:
                    return  str (a)+"(x - "+str(-1*x1) +")x"
            else:
                if x2<0:
                        return  str (a)+"x(x + "+str(-1*x2) +")"
                elif x2>0:
                    return  str (a)+"x(x - "+str(-1*x2) +")"
#a*x2+b*x+c

a = int (input("a="))
b = int (input("b="))
c = int (input("c="))

#(-b+-gyök(b2-4ac)) / 2a

#print(math.sqrt(3))

x1=""
x2=""

diszkriminans=b*b-4*a*c
if diszkriminans<0:
    print("nincs megoldás")
elif diszkriminans==0:
    megoldas=-b /(2*a)
    x1=megoldas
    x2=megoldas
    print("1 megoldas : {}".format(megoldas))
else:
    x1=(-b+math.sqrt(diszkriminans)) / (2*a)
    x2=(-b-math.sqrt(diszkriminans)) / (2*a)
    print("2 megoldás: x1:(), x2:{}".format(x1,x2))
   
#gyok=math.sqrt(b*b-4*a*c)
#print(gyok)
print (egyenlet(a,b,c))

#a*(x-x1)*(x-x2)=0

print(gyokTenyezosSzorzat(a,x1,x2))
print(a)
print(x1)
print(x2)
