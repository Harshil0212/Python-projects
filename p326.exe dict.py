marks={"ram":33,"rahul":45,"devesh":30,"jayul":34}
n=input("enter key name==")
for k,v in marks.items():
    if k==n:
        print(k,"\t",v,"\tyes it's already exist")
