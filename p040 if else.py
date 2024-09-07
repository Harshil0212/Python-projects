print("press + for addition")
print("press - for substraction")
print("press * for multiplication")
print("press / for division")

op=input("entre option=")

if op=="+":
    number1=float(input("entre number="))
    number2=float(input("entre number="))
    print("addition=", number1+number2)

elif op =="-":
    number1 = float(input("entre number="))
    number2 = float(input("entre number="))
    print("substraction=", number1-number2)

elif op =="*":
    number1 = float(input("entre number="))
    number2 = float(input("entre number="))
    print("multiplication=", number1*number2)

elif op =="/":
    number1 = float(input("entre number="))
    number2 = float(input("entre number="))
    print("division=", number1/number2)

else:
    print("wrong option")