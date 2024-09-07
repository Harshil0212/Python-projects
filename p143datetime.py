import time
current=time.localtime(time.time())

h=current.tm_hour

if h<12:
    print(h-12,"AM")
else:
    print(h-12,"PM")