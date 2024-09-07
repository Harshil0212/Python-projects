n=int(input("enter limit="))
t=0
for i in range(1,101):
    if i%2==0:
        t=t+i

print("Total = ",t)
