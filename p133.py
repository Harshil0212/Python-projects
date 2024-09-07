while True:
    print(" -*- "*40)
    print("press s for square")
    print("press c for cube")
    print("press 3 for exit")
    op=input("enter option=").lower()
    print(" -*- "*40)
    if op=="s":
        number=int(input("enter number="))
        print("square=",number*number)
    elif op=="c":
        number=int(input("enter number="))
        print("cube=",number*number*number)
    elif op==3:
        print("Bye")
        break
    else:
        print("wrong option")