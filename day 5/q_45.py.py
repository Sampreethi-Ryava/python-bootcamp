#print sum of digits using ascii values
str=input()
sum=0
for i in (str):
    if(ord(i)>=48 and ord(i)<=57):
     sum+=int(i)
print(sum)

