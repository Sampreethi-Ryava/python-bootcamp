a=int(input())
b=int(input())
c=a*b
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)
lcm=c//a
print("LCM of 2 numbers is:",lcm)