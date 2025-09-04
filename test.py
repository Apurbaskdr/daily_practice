from collections import Counter

ls=[1,2,3,4,5,2,3,4]
freq=Counter(ls)
#val=freq.values()
val=all(v <= 1 for v in freq.values())
print (val)