ls1=[1,1,1,1,2,3,4,5,5,5,3,4,6,7]
ls1.sort()
i=0
ls1_len=len(ls1)
i=0
while i<len(ls1):
    ele=ls1[i]
    new_list=ls1[i+1:]
    print ("new_list:",new_list)
    for j in range(len(new_list)-1):
        if new_list[j]==ele:
            ls1.remove(new_list[j])
            print (ls1)
    i+=1
    
print(ls1)