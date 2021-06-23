a=int(input())
b=bin(a)
s=b[2:].split('0')
lst=list()
for i in s:
    l=len(i)
    lst.append(l)
print(max(lst))
#lst=list()
#i=0
#while i<(l-1):
#    count=1
#    if(s[i]==1):
#        while(s[i]==s[i+1]):
#            count=count+1
#            i=i+1
#            if(i+1==l):
#                break
#lst.append(count)
#    else:
#        i=i+1
#        continue
#    lst.append(count)
#    i=i+1
    #list.append(count)
