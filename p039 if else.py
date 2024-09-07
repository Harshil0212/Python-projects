print("press p for pizza")
print("press a for panipuri")
print("press @ for dhosa")
print("press m for paratha")

op=input("entre option=")

if op=="p":
    print("Price of Pizza 300")
    qty=int(input("Enter qty of pizza ->"))
    print("Bill of Pizza = ",qty*300)

elif op=="a":
    print("price of panipuri 100")
    qty=int(input("entre qty of panipuri="))
    print("bill of panipuri=",qty*100)

elif op=="@":
    print("prize of dhosa 200")
    qty=int(input("entre qty of dhosa="))
    print("bill of dhosa=",qty*200)

elif op=="m":
    print("prize of paratha 250")
    qty=int(input("entre qty of paratha="))
    print("bill of paratha",qty*250)

else:
    print("not option")
