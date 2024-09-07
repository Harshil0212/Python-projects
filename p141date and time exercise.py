import time
current=time.localtime(time.time())

h=current.tm_hour
m=current.tm_min
s=current.tm_sec

if h<12:
    print(h,":",m,":",s,"good morning")

elif h>12 and h<18:
    print(h,":",m,":",s,"good afternoon")

else:
    print(h,":",m,":",s,"good night")