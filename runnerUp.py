n=int(input())
l=list(map(int,input().split(" ")))
l.sort(reverse=True)
v=max(l)
while max(l)==v:
    l.remove(max(l))
#print(l)
print(max(l))
#c=0
#flag=0
#for i in l:
#    if(i==v):
#        c=c+1
#        if(c>1):
#            l.remove(i)
#            flag=0
#    else:
#        flag=1
#if(flag==0):
#    print(l[1])
#if(flag==1):
#    print(l[1])
