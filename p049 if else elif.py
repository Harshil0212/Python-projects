print("press pizza for pizza")
print("press paratha for paratha")
print("press dhosa for dhosa")
print("press both for both")

op=input("entre option=").lower()
if op=="pizza":

    print("pizza prize is 220")
    qty=int(input("entre qty of pizza="))
    if qty>5:
        print("bill=",qty*220)
    else:
        print("bill=",qty*240)

elif op=="paratha":
    print("paratha prize is 100")
    qty=int(input("entre qty of paratha="))
    if qty>5:
        print("bill=",qty*100)
    else:
        print("bill=",qty*120)

elif op=="dhosa":
    print("dhosa prize is 120")
    qty=int(input("entre qty of dhosa="))
    if qty>5:
        print("bill=",qty*120)
    else:
        print("bill=",qty*140)

elif op=="both":

    b1=0
    b2=0
    b3=0

    qty1=int(input("entre qty of pizza="))
    print("pizza prize is 220")
    if qty1>5:
        b1=qty1*220
        print("bill=",b1)
    else:
        b1=qty1*240
        print("bill=",b1)

        qty2=int(input("entre qty of paratha="))
        print("paratha prize is 100")
        if qty2>5:
            b2=qty2*100
            print("bill=",b2)
        else:
            b2=qty2*120
            print("bill=",b2)

            qty3=int(input("entre qty of dhosa="))
            print("dhosa prize is 120")
            if qty3>5:
                b3=qty3*120
                print("bill=",b3)
            else:
                b3=qty3*140
                print("bill=",b3)

                total=b1+b2+b3
                print("total=",total)


else:
    print("wrong option")





