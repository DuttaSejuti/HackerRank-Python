n=int(input())
c=list(map(int,input().rstrip().split()))
jump=0
l=len(c)
#print(l)
i=0
while(i<l-1):
    if(i<l-2 and c[i+2]==0):
        i=i+2
        jump=jump+1
    else:
        i=i+1
        jump=jump+1

print(jump)
