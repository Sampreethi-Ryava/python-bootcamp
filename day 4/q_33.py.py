#write a program to find whether the given number is prime or not a prime 
a=int(input())
count=0
r=a**0.5
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if (count==0):
    print("prime")
else:
    print("not a prime")