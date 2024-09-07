marks={"ram":33,"rahul":15,"devesh":30,"jayul":34,"jiya":16,"sadhana":11}
for k,v in marks.items():
    if v>18:
        print(k,"\t",v,"\t pass")
    else:
        print(k,"\t",v,"\t fail")