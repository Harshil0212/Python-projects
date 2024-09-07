age=int(input("entre your age="))
gender=input("entre your gender=").lower()
maritalstatus=input("entre your maritalstatus=").lower()

if gender=="female":
    print("work in only urban area")

elif gender=="male" and age>20 and age<40:
    print("work in anywhere")

elif gender=="male" and age>40 and age<60:
    print("work in urban area only")

else:
    print("error")