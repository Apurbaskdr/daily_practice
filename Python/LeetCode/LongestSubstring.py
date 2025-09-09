from collections import OrderedDict

def LongestSubstring(s):
    ls=list(s)
    #print (ls)
    ls1=''.join(list(OrderedDict.fromkeys(ls)))

    f=0
    if len(ls1) == len(ls) or len(ls1) < 3:
        return (len(ls1))
    for i in range(1,len(ls)-2):
        if ls[i] == ls[i+1]:
            f=1
            nls=list(OrderedDict.fromkeys(ls))
            break
        else:
            nls=ls

    lng=len(nls)
    #print (lng)
    i=0
    mx=[]
    while i <  lng:
        pls=nls[i:]
        #print (pls)
        j=0
        ppls=[]
        ns=''
        while j<len(pls):
            ppls.append(pls[j])
            if len(ppls) == len(ls1) and f==1:
                print('Yes')
                break
            else:
                ns=''.join(list(OrderedDict.fromkeys(ppls)))
                
            
            #print(ppls)
            #print(ls1)
            j=j+1
        print ('ns: ',ns)
        if len(mx)>len(ns):
            pass
        else:
            mx=ns
        i=i+1
    return len(mx)



s='ckilbkd'
res=LongestSubstring(s)
print(res)