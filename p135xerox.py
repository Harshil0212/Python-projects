b1=0
b2=0
while True:
    print("\n\n")
    print(" -*- "*10)
    print("press 1 for xerox")
    print("press 2 for typing")
    print("press 3 for exit")

    op=int(input("enter option="))
    print(" -*-"*10)

    if op==1:
        print("xerox price is 5")
        qty=int(input("enter qty of xerox="))
        if qty>50:
            b1=qty*5
            print("bill of xerox=",b1)
        else:
            b1=qty*7
            print("bill of xerox=",b1)

    elif op==2:
        print("typing price is 15")
        qty=int(input("enter qty of typing="))
        if qty>50:
            b2=qty*15
            print("bill of typing=",b2)
        else:
            b2=qty*20
            print("bill of typing=",b2)

    elif op==3:
            print("bill of total=",b1+b2)
            print("bye")
            break

    else:
        print("wrong option")
         
















