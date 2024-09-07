print("press 1 for addtion")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")

op=int(input("entre number="))

if op==1:
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1+number2
    print("total=",total)

elif op==2:
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1-number2
    print("total=",total)

elif op==3:
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1*number2
    print("total=",total)

elif op==4:
    number1=float(input("entre 1 number="))
    number2=float(input("entre 2 number="))
    total=number1/number2
    print("total=",total)

else:
    print("wrong option")