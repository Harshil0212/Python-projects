print("Press s for square")
print("Press c for cube")
op=input("Enter option =>")

if op=="s":
    number=float(input("entre number="))
    print("square=",number*number)
elif op=="c":
    number=float(input("entre number="))
    print("cube=",number*number*number)
else:
    print("Wrong opt")