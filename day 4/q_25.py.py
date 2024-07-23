#mr-x is trying to create a new password for instagram account these are the required conditions for creating a new password
#case-1:min length-8&max length-15,case-2:only @,/ is allowed in a password,case-3:no spaces are allowed,case-4:only alpha numerics are allowed you are supposed to 
#print weak if length is exact 8,medium-length is between 8to12,strong-if length is between 12to15

str=input()
count=0
len=len(str1)
if(len(str)>=8 and len(str)<=15):
    print("password is allowed")
else:
    print("follow the conditions")