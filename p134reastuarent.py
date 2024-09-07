b1=0
b2=0
b3=0
b4=0
b5=0
while True:
    print(" -*- "*10)
    print("press 1 for pizza")
    print("press 2 for dhosa")
    print("press 3 for panipuri")
    print("press 4 for paratha")
    print("press 5 for bhajipav")
    print("press 6 for exit")
    print(" -*- "*10)

    op=int(input("enter option="))

    if op==1:
        print("pizza price is 200")
        qty=int(input("enter qty of pizza="))
        b1=200*qty
        print("bill of Pizza=",b1)

    elif op==2:
        print("dhosa price is 70")
        qty=int(input("enter qty of dhosa="))
        b2=70*qty
        print("bill of dhosa=",b2)

    elif op==3:
        print("panipuri price is 50")
        qty=int(input("enter qty of panipuri="))
        b3=50*qty
        print("bill of panipuri=",b3)

    elif op==4:
        print("paratha price is 170")
        b4=170*qty
        qty=int(input("enter qty of paratha="))
        print("bill of paratha=",b4)

    elif op==5:
        print("bhajipav price is 90")
        b5=90*qty
        qty=int(input("enter qty of bhajipav="))
        print("bill of bhajipav=",b5)

    elif op==6:
        print("bill of Pizza=",b1)
        print("bill of dhosa=",b2)
        print("bill of panipuri=",b3)
        print("bill of paratha=",b4)
        print("bill of bhajipav=",b5)
        print("Final bill is=",b1+b2+b3+b4+b5)
        print("bye")
        break

    else:
        print("wrong option")


