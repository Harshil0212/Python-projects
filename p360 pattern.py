n=int(input("enter limit="))
k=n
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(k,end=" ")
    print(" ")
    k-=1