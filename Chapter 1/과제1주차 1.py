import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

d = b*b-4*a*c

if d < 0:
    print("해가 없습니다")
else:
    x1 = ((-b)+math.sqrt(d))/2*a
    x2 = ((-b)-math.sqrt(d))/2*a
    print("x1=",x1,"x2=",x2)
