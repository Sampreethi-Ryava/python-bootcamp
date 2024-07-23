#Mr.z is selected for olympics.He is participating in swimming competition only one winner is selected in the competition and Mr.z got selected.Mr-X&Y are friends of Z
#Mr-z is participating in badminton Mr.y is participating in tabletennis.According to selection committee the reqirement for badminton player are
#height-140cm,weight-factors of 2,body fat is less than 12%.According to selection committee the requirement for tabletennis are height-minimum 118-148cm,weight-factors
# of no.of medals won by mr-z,bodyfat-14%.According to the previous history z participated in 14games out of which he is having success rate of 65%.Write a program to check
#whether mr-x,y,z from india travelled in a same plane 
height_of_x=int(input())
height_of_y=int(input())
weight_of_x=int(input())
weight_of_y=int(input())
x_selected=0
y_selected=0
if(height_of_x==140 and weight_of_x%2==0):
    x_selected+=1
    if((height_of_y<148 and height_of_y>118)and weight_of_y%7==0):
        y_selected+=1
        if(y_selected==1 and x_selected==1):
            print("x,y and z will meet in airplane")
        else:
            print("not meet")

