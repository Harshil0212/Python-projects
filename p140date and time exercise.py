import time
current=time.localtime(time.time())

y=current.tm_year

if y%4==0:
    print(y,"it is not leap year")
else:
    print("yes it is leap year")
