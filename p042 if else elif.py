print("press c for area of circle")
print("press t for area od triangle")
op=input("entre option=")
if op=="c" or op=="C":
     r=float(input("entre radius="))
     print("area of circle=",r*r*3.14)
elif op=="t" or op=="T":
    h=float(input("entre height="))
    b=float(input("entre base="))
    print("area of triangle=",h*b*0.5)
else:
    print("wrong opt")