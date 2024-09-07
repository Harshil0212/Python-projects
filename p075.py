prize=int(input("enter prize="))

b1=0
b2=0
b3=0

if prize>10000:
    dis=prize*0.20
    print("Discount amt = ",dis)
    print("Before discount Bill =",b1)
    print("After discount Bill =",b1-dis)

elif prize>7000 or prize<10000:
    b2=prize*0.15
    print("bill=",b2)

elif prize>=7000:
    b3=prize*0.10
    print("bill=",b3)

total = b1+b2+b3
print("total=",total)