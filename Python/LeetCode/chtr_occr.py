str1='Ananya'
str1_list=list(str1.lower())
print(str1_list)
distinct_value=list(set(str1_list))
i,frq_list=0,[]
while i<len(distinct_value):
    count=0
    for st in str1_list:
        if st == distinct_value[i]:
            count += 1
    frq_list.append(count)
    i+=1
    
list_frq=list(zip(distinct_value,frq_list))
print(list_frq)    