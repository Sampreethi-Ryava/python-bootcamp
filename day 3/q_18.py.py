#find the elements that is present in k+ith index k=3;n=2-k+n index
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
len=len(my_list)
if(len<k+n): 
    print("error")
else:                                                                  
    for i in range(0,len):
        print(my_list[k+n],end=" ")
        break

