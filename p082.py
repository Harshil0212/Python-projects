trafficcolour=input("entre colour of traffic light=")

if trafficcolour=="green":
    print("car is allowed to go")

elif trafficcolour=="yellow":
    print("car has to wait")

elif trafficcolour=="red":
    print("car has to stop")

elif trafficcolour=="black" or trafficcolour=="blue" or trafficcolour=="white":
    print("unricognized colour")

else:
    print("wromg option")