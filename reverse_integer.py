num=1534
num_pos=0
max_range_pos=2**31-1
max_range_neg=-2**31

if num < 0:
    f='Yes'
    num_pos=num*(-1)
else:
    f='No'
    num_pos=num
new_num=0
while num_pos > 0:
    new_num=new_num*10+num_pos%10
    num_pos=num_pos//10
if f=='Yes':
    new_num=new_num*-1
else:
    new_num=new_num
    #print(new_num)


if new_num<max_range_pos and new_num > max_range_neg:
    print (new_num)
else:
    print (0)
#print (new_num)