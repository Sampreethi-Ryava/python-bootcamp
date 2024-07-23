#mother gave 700 to mr.x and asked to bring fruits cost of one apple is 15,cost of banana is 4 and the cost of orange is 5 the total number of apples buyed are 10,banana is 2 dozens and orange is 8
a=int(input())
b=int(input())
c=int(input())
acost=a*5
bcost=b*4
ccost=c*5
total=acost+bcost+ccost
print(f"total:(total)")
if(total<=700):
    print("x is not being cheated")
else:
    print("x is being cheated")