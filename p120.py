s=1
n=int(input("enter limit="))
for i in range(n,0,-1):
    print(i,end=" * ")
    s=s*i
print("\nsum=",s)