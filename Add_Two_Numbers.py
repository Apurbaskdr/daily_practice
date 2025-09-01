def add_two_numbers(ls1,ls2):
    ls1.reverse()
    ls2.reverse()
    print(ls1,ls2)
    num1,num2=0,0
    for i in ls1:
        num1=num1*10+i
    for j in ls2:
        num2=num2*10+j
    print(num1)
    print(num2)
    res=num1+num2
    resln=digln(res)
    print(resln)
    return resln.reverse()

def digln(n):
    return list(map(int,str(n)))




ls1=[2,4,3]
ls2=[5,6,4]
result=add_two_numbers(ls1,ls2)
print(result)