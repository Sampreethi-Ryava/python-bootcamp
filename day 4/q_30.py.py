#find the leap year between provided range
year=int(input())
if(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")