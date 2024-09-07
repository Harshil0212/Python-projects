salary=int(input("entre your salary=>"))
year=int(input("year of service=>"))

if year>5:
    print("bonus amount=>",salary*0.5)

elif year<5:
    print("bonus amount=>",salary*0.3)

else:
    print("not bonus")