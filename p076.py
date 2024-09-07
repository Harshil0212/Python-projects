age=int(input("entre age="))
gender=input("entre gender=")

if age>=18 and age<30 or gender=="m":
    print("days=700")

elif age>=18 and age<30 or gender=="f":
    print("days=750")

elif age>=30 and age<40 or gender=="m":
    print("days=800")

elif age>=30 and age<40 or gender=="f":
    print("days=850")

else:
    print("wrong option")

