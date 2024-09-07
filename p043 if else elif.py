print("press circle for area of circle")
print("press triangle for area od triangle")
op=input("entre option=").lower()
if op=="circle":
     r=float(input("entre radius="))
     print("area of circle=",r*r*3.14)
elif op=="triangle":
    h=float(input("entre height="))
    b=float(input("entre base="))
    print("area of triangle=",h*b*0.5)
else:
    print("wrong opt")