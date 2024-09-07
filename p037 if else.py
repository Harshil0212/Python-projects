print("press 1 for pizza")
print("press 2 for panipuri")
print("press 3 for dhosa")
print("press 4 for paratha")

op=float(input("entre option="))

if op==1:
    print("Price of Pizza 300")
    qty=int(input("Enter qty of pizza ->"))
    print("Bill of Pizza = ",qty*300)

elif op==2:
    print("price of panipuri 100")
    qty=int(input("entre qty of panipuri="))
    print("bill of panipuri=",qty*100)

elif op==3:
    print("prize of dhosa 200")
    qty=int(input("entre qty of dhosa="))
    print("bill of dhosa=",qty*200)

elif op==4:
    print("prize of paratha 250")
    qty=int(input("entre qty of paratha="))
    print("bill of paratha",qty*250)

else:
    print("not option")
