def add(number1,number2):
    print("addition=",number1+number2)

def max2(number1,number2):
    if number1>number2:
        print(number1,"is greater")
    else:
        print(number2,"is greater")


number1=int(input("enter number1="))
number2=int(input("enter number2="))
add(number1,number2)
max2(number1,number2)
