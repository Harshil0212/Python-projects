print("press + for addtion")
print("press - for substraction")
print("press * for multiplication")
print("press / for division")

op=input("entre number=")

if op=="+":
    number1=int(input("entre 1 number="))
    number2=int(input("entre 2 number="))
    total=number1+number2
    print("total=",total)

elif op=="-":
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1-number2
    print("total=",total)

elif op=="*":
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1*number2
    print("total=",total)

elif op=="/":
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1/number2
    print("total=",total)

else:
    print("wrong option")