while True:
    print(" -*- "*100)
    print("press + for addtion")
    print("press - for substraction")
    print("press / for division")
    print("press * for multiplication")
    print("press e for exit")
    op=input("enter option=")
    print(" -*-"*100)

    if op=="+":
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("addition=",number1+number2)

    elif op=="-":
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("substraction=",number1-number2)

    elif op=="/":
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("division=",number1/number2)

    elif op=="*":
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("multiplication=",number1*number2)

    elif op=="e":
        print("bye")
        break

    else:
        print("wrong option")


