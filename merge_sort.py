def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid=len(ls)//2
    left=ls[:mid]
    right=ls[mid:]
    l_ls=merge_sort(left)
    r_ls=merge_sort(right)
    print("left ls:",l_ls)
    print("right_ls:",r_ls)
    return merge(l_ls,r_ls)

def merge(left,right):
    new=[]
    i,j=0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

ls=[5,2,4,3,1,6,9,8,7]
merged=merge_sort(ls)
print(merged)