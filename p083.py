integer=int(input("entre integer="))


if integer%2==1:
    print("weird")

elif integer%2==0 and integer>2 and integer<5:
    print("not weird")

elif integer%2==0 and integer>6 and integer<20:
    print("weird")

elif integer%2==0 and integer>20:
    print("not weird")

else:
    print("not option")