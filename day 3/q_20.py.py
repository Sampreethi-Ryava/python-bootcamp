#maximum and minimum numbers
my_list=list(map(int,input().split()))
#print(max(my_list))
#maxi=my_list[0]
#for i in range(0,len(my_list)):
 #   if(my_list[i]>maxi):
  #      maxi=my_list[i]
   # print(maxi)


min=my_list[0]
for i in range(0,len(my_list)):
  if(my_list[i]<min):
     min=my_list[i]
     print(min)
     