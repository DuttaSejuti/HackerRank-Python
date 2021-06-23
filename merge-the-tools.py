s=str(input())
k=int(input())
l=len(s)
factor=int(l/k)
lst=list()
lst2=list()
while(l>0):
    lst.append(s[:factor])
    s=s[factor:]
    l=len(s)
print(lst)
new_str=''
for w in lst:
    for i in range(0,len(w)):
        if(w[i]==w[i+1]):
