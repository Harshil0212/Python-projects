while True:
    print("*"*40)
    print("press 1 for square")
    print("press 2 for cube")
    print("press 3 for exit")
    op=int(input("enter option="))
    print("*"*40)
    if op==1:
        number=int(input("enter number="))
        print("square=",number*number)
    elif op==2:
        number=int(input("enter number="))
        print("cube=",number*number*number)
    elif op==3:
        print("Bye")
        break
    else:
        print("wrong option")
