#perform append,pop,sort,hello length in one program
my_list=list(map(int,input().split(" ")))
print("enter 1 for append")
print("enter 2 for pop")
print("enter 3 for sort")
print("enter 4 for length")
chioce=int(input())
if (chioce==1):
    my_list.append(47)
    print(*my_list)
elif(chioce==2):
     my_list.pop(3)
     print(*my_list)    
elif(chioce==3):
     my_list.sort()
     print(*my_list)
else:
     print(f"good mrng length of the list {len(my_list)}")    