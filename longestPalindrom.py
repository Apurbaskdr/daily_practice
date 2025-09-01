def pal(s):
    list_str=list(s)
    lenth_list=len(list_str)
    i=0
    final_str=''
    while i < lenth_list:
        sub_list=list_str[i:]
        j=0
        list_to_test=[]
        
        while j < len(sub_list):
            list_to_test.append(sub_list[j])
            str_to_test=''.join(list_to_test)
            reverse_list_to_test=str_to_test[::-1]
            #print (reverse_list_to_test)
            if str_to_test == reverse_list_to_test and len(final_str) < len(str_to_test):
                    #print("Inside the if condition:",str_to_test)
                    #if :
                    #        print("inside the lenth test")
                    final_str=str_to_test
                    j+=1           
            else:
                 j=j+1
        i+=1
    return final_str


s='babadada'
ss=pal(s)
print(ss)