#given an space separated integer list finf the average of elements present in the even index
my_list=list(map(int,input().split(" ")))
sum=0
n=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
       sum+=my_list[i]

print(sum/i)