def add():
    number1=int(input("enter number1="))
    number2=int(input("enter number2="))
    print("addition=",number1+number2)

def max2():
    number1=int(input("enter number1="))
    number2=int(input("enter number2="))
    if number1>number2:
        print(number1,"is greater")
    else:
        print(number2,"is greater")

def square():
    number = int(input("enter number="))
    print("square=", number * number)


def table():
 number=int(input("enter number="))
 for i in range(1,11):
    print(number,"*",i,"==",number*i)

def oddeven():
    number=int(input("enter number="))
    if number%2==0:
        print("even")
    else:
        print("odd")

def posneg():
    number=float(input("enter number="))
    if number>0:
        print("positive")
    else:
        print("negative")

def add():
    number1=int(input("enter number1="))
    number2=int(input("enter number2="))
    number3=int(input("enter number3="))
    print("addition=",number1+number2+number3)

def max3():
    number1=int(input("enter number1="))
    number2=int(input("enter number2="))
    number3=int(input("enter number3="))

    if number1>number2 and number1>number3:
        print(number1,"is greater")

    elif number2>number1 and number2>number3:
        print(number2,"is greater")

    else:
        print(number3,"is greater")

def areaoftri():
    h=float(input("enter height="))
    b=float(input("enter base="))
    print("area of triangle=",h*b*0.5)

def areaofcircle():
    r=float(input("enter radius="))

    print("area of circle=",3.14*r*r)


add()
add()
max2()
square()
table()
oddeven()
posneg()
max3()
areaoftri()
areaofcircle()

