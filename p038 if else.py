name=str(input("entre your name="))
print("name=",name)

classnumber=int(input("entre your classnumber="))
print("classnumber=",classnumber)

maths=int(input("entre your maths marks="))
hindi=int(input("entre your hindi marks="))
english=int(input("entre your hindi marks="))

total=maths+hindi+english
avg= total/3

print("total=",total)
print("avg",total/3)

if total>90:
    print("A grade")

elif total>80:
    print("B grade")

elif total>70:
    print("C grade")

elif total>60:
    print("D grade")

elif total<40:
    print("fail")

else:
    print("not option")
