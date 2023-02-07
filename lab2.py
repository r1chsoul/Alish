import math
x=int(input("Peremennaya x:"))
t=int(input("Peremennaya t:"))
z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z=|{0:.2f}".format(z))