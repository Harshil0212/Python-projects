eng=int(input("entre eng mark="))
hindi=int(input("entre hindi mark="))
maths=int(input("entre maths mark="))
total=eng+hindi+maths
print("total=",total)

if total>100:
    print("A grade")

elif total>50 and total<100:
    print("B grade")

elif total>0 and total<50:
    print("C grade")

else:
    print("wrong option")

