print("press type for type")
print("press xerox for xerox")
print("press both for both")

op=input("entre number=").lower()

if op=="type":
    print("type prize is 15")
    qty2=int(input("entre qty of type="))
    print("bill=",qty2*15)
elif op=="xerox":
    print("xerox prixe is 5")
    qty1=int(input("entre qty of xerox="))
    print("bill=",qty1*5)

elif op=="both":
    qty1=int(input("entre xerox qty="))
    qty2=int(input("entre type qty="))
    b1=qty1*5
    b2=qty2*15
    print("bill of xerox=",b1)
    print("bill of type=",b2)
    total=b1+b2
    print("total=",total)


else:
    ("not option")









