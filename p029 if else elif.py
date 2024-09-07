number1=float(input("enter value="))
number2=float(input("entre value="))
number3=float(input("entre value="))
if number1>number2 and number1>number3:
    print("number1 is greater")
elif number2>number3 and number2>number1:
    print("number 2 is greater")
elif number3>number1 and number3>number2:
    print("number 3 is greater")


else:
    print("are are equal")