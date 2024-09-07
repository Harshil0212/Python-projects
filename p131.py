while True:
    print(" -*- "*100)
    print("press 1 for addtion")
    print("press 2 for substraction")
    print("press 3 for division")
    print("press 4 for multiplication")
    print("press 5 for exit")
    op=int(input("enter option="))
    print(" -*- "*100)

    if op==1:
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("addition=",number1+number2)

    elif op==2:
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("substraction=",number1-number2)

    elif op==3:
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("division=",number1/number2)

    elif op==4:
        number1=int(input("enter number1="))
        number2=int(input("enter number2="))
        print("multiplication=",number1*number2)

    elif op==5:
        print("bye")
        break

    else:
        print("wrong option")


