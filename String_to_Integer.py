src_str="-42"
src_list=[]
#src_list=list(src_str)
for i in src_str:
    if i == '-' or i== '+':
        new_src_str=src_str[i:]
    elif i == '0':
        new_src_str=src_str[i:]
    elif i.isdigit():
        src_list.append(i)
    else:
        break

print (src_list)

'''src_list=[]
for i in src_str:
    if i == "0":
    if i.isdigit():
        src_list.append(i)
    else:
        #print (False)
        break
print (src_list)'''