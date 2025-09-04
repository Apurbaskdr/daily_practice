"""You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct."""



def distinctArray(arr):
    lnArr=len(arr)
    arrSet=list(set(arr))
    count=0
    
    if lnArr == len(arrSet):
        return 0
    while lnArr > 0:
        subArr=arr[3:]
        print (subArr)
        count +=1
        if len(list(set(subArr)))== len(subArr):

            return count
        elif len(subArr)==2:
            count+=1
            return count
        else:
            arr=subArr
            lnArr -=3
    return count




arr=[1,2,3,4,2,3,3,5,7]
res=distinctArray(arr)
print(res)