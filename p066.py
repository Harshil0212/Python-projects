temp=int(input("entre temperature="))

if temp<0:
    print("freezing atmosphere")

elif temp>0 and temp<10:
    print("very cold atmosphere")

elif temp>10 and temp<20:
    print("cold atmosphere")

elif temp>20 and temp<30:
    print("normal atmosphere")

elif temp>30 and temp<40:
    print("hot atmosphere")

elif temp>40:
    print("very hot")

else:
    print("wrong option")