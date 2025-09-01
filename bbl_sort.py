def bbl_sort(ls):
    if len(ls)<=1:
        return ls
    for i in range(len(ls)):
        for j in range(0,len(ls)-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls

ls=[5,8,6,7,2,3,4,1]
r=bbl_sort(ls)
print(r)