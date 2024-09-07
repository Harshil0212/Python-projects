print("press 1 for addition")
print("press 2 for multiplication")
print("press 3 for dividion")
print("press 4 for substraction")
op=float(input("entre option="))

if op==1:
    number1=float(input("entre number="))
    number2 = float(input("entre number="))
    print("addition=",number1+number2)

elif op==2:
    number1=float(input("entre number="))
    number2=float(input("entre number="))
    print("multiplication=",number1*number2)

elif op==3:
    number1=float(input("entre number="))
    number2=float(input("entre number="))
    print("dividion=",number1/number2)

elif op==4:
    number1=float(input("entre number="))
    number2=float(input("entre number="))
    print("substraction=",number1-number2)

else:
    print("wrong option")
