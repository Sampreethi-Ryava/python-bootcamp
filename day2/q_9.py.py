#find the average of elements 
my_list=list(map(int,input().split(" ")))
avg=0
sum=0
for i in range(0,len(my_list),2):
    if(i%2==0):
      sum+=my_list[i]
      avg=sum/len(my_list)
 print(avg)