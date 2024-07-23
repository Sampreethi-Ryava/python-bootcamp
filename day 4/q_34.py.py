#sort it print first half ascending and second descending
n=list(map(int,input().split(" ")))
n.sort()
for i in range(0,(len(n))//2):
    print(n[i],end=" ") 
for i in range((len(n))//2,len(n)):
    print(n[i],end=" ")
