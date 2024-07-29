#write a code to remove all brackets from the given algebraic equation 
str=input()
for i in(str):
    if(ord(i)==40 or ord(i)==41 or ord(i)==90 or ord(i)==91 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end="")
        

