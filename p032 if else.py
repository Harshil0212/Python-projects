print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    number=float(input("entre number="))
    print("square=",number*number)
elif op==2:
    number=float(input("entre number="))
    print("cube=",number*number*number)
else:
    print("Wrong opt")