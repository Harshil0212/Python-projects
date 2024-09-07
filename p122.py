s=0
n=int(input("enter limit="))
for i in range(1,n+1):
     print(i*i*i,end=" + ")
     i=i*i*i
     s=i+s
print("\nsum=",s)