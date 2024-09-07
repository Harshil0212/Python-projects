s=0
n=int(input("enter limit="))
for i in range(1,n+1):
    print("1/",i,end=" + ")
    s=s+1/i
print("\nsum=",s)