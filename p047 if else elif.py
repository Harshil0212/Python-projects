print("press type for type")
print("press xerox for xerox")
print("press both for both")

op=input("entre number=").lower()

if op=="type":
    print("type prize is 15")
    qty=int(input("entre qty of type="))
    if qty>50:
        print("bill = ",qty*15)
    else:
        print("bill = ", qty * 20)
elif op=="xerox":
    print("xerox prize is 5")
    qty=int(input("entre qty of xerox="))
    if qty>50:
        print("bill=",qty*5)
    else:
        print("bill=",qty*7)
elif op=="both":
    b1=0
    b2=0
    qty1=int(input("entre xerox qty="))
    if qty1>50:
        b1=qty1*5
        print("bill =",b1)
    else:
        b1=qty1*7
        print("bill=",b1)
    qty2=int(input("entre type qty="))
    if qty2>50:
        print("bill=",qty2*15)
    else:
        print("bill=",qty2*20)
    total=b1+b2
    print("total=",total)


else:
    ("not option")

