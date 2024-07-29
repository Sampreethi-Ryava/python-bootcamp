# print reverse of numerics present in a given string
#case:hello1234
#     4321
str=input()
n=" "
rev=0
check="0123456789"
for i in(str):
    n= int(n.append(i))
while n>0:
    r=n%10
    rev=10*rev+r
    n=n/10
print(rev)
