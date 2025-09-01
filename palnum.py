def palnum(num):
    i=num
    rev=0
    while i>0:
        rem=i%10
        rev=rev*10 + rem
        i=i//10

    if rev == num:
        return "Pallindrom"
    else:
        return "Not Pallindrom"


num=121
res=palnum(num)
print (res)