number1=int(input("entre number 1="))
number2=int(input("entre number 2="))
number3=int(input("entre number 3="))

if number1>number2 and number1>number3:
    print("number 1 is greater")

elif number2>number1 and number2>number3:
    print("number 2 is greater")

elif number3>number1 and number3>number2:
    print("number 3 is greater")

else:
    print("wrong option")