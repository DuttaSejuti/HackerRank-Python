n=input()
#print(n.swapcase())
str1=""
for i in n:
    if(i.islower()):
        str1=str1+i.upper()
    else:
        str1=str1+i.lower()
#s=''.join(map(str,new_list))
print(str1)
