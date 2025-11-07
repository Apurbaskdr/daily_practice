ls1=[1,1,1,1,2,3,4,5,5,5,3,4,6,7]
ls1_set=list(set(ls1))
print(ls1_set)
len_ls1=len(ls1_set)
print(len_ls1)
max_num,i,frq_list=0,0,[]

while i<len_ls1:
    count=0
    for j in ls1:
        if j == ls1_set[i]:
            count+=1
    frq_list.append(count)
    if max_num<count:
        max_num=count
        val=ls1_set[i]
    i+=1
print (frq_list)
merge_list=list(zip(ls1_set,frq_list))
print(merge_list)
print(max_num)
print(val)