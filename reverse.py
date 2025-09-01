def rev(ls):
    mid=len(ls)//2
    ln=[]
    for i in range(len(ls)-1,-1,-1):
        ln.append(ls[i])
    return ln

ls=[1,2,3]
res=rev(ls)
print(res)