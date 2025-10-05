nums=[-3,-12,-3,-9,14,4,8,-4,11,4,7,-8,-5,4,7,-12,2,9,6,-12,8,-5,-14,5,3,11,14,-6,-5,10,-8,0,6,5,6,5,-6,-9,-13,12,2,1,-10,13,13,4,-14,0,-2,0,-5,13,10,-12,-5,-9,-15,-13,-8,-13,12,-1,-6,3,11,7,-14,-9,14,10,10,-7,-4,-15,-9,-6,4,-15,2,10,-8,12,0,9,-14,11,-15,8,13,14,10,2,-9,-10,13,-13,12,14,-15,3,1,11,12,12,11,10]


if len(nums) < 3:
    print ("Length is short of 3")
i=0
new_ls=[]
for i in range(len(nums)-2):
    frst_ele=nums[i]
    
    for j in range(i+1,len(nums)-1):
        snd_ele=nums[j]
        
        #print (f_ele, s_ele)
        for k in range(j+1,len(nums)):
            trd_ele=nums[k]
            sub_ls=[]
            
            res=sum((frst_ele, snd_ele, trd_ele))
            sub_ls.append(frst_ele)
            sub_ls.append(snd_ele)
            sub_ls.append(trd_ele)
            sub_ls.sort()
            if res==0 and sub_ls not in new_ls:
                new_ls.append(sub_ls)
            
print (new_ls)