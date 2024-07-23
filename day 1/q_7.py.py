#driving license
#age=25
age=int(input())
if(age>=18 and age<24):
    print("only two wheelers")
elif(age>=24 and age<45):
    print("two and four wheelers")
else:
    print("all")