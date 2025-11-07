str1='Apa'
r_str1=''
for i in str1:
    r_str1=i+r_str1
print (r_str1)
if str1.lower() == r_str1.lower():
    print ("Palindrom")
else:
    print ("No")