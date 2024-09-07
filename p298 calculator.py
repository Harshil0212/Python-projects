def calculator():
    #input two numbers from the user

    num1=int(input("enter number 1="))
    num2=int(input("enter number 2="))

    #input operation choice from the user
    print("press 1 for addtion")
    print("press 2 for substraction")
    print("press 3 for multiplication")
    print("press 4 for division")

    choice=input("enter your choice=")

    #perform the calculation based on the chosen operation

    if choice=="1":
        result=num1+num2
        print("result=",result)

    elif choice=="2":
        result=num1-num2
        print("result=",result)

    elif choice=="3":
        result=num1*num2
        print("result=",result)

    elif choice=="4":
        if num2 !=0:
            result=num1/num2
            print("result=",result)
        else:
            print("error:divisible by 0 is not allowed")

    else:
        print("wrong option")



#calling this function
calculator()