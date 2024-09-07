print("press 1 for area of circle")
print("press 2 for area od triangle")
op=float(input("entre option="))
if op==1:
     r=float(input("entre radius="))
     print("area of circle=",r*r*3.14)
elif op==2:
    h=float(input("entre height="))
    b=float(input("entre base="))
    print("area of triangle=",h*b*0.5)
else:
    print("wrong opt")