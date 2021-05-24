steps = int(input().strip())
path = input()
res1=0
res2=0
for i in range(steps):
    if(path[i]=='U'):
        res1=res1+1
        #print(res1)
    if(path[i]=='D'):
        res1=res1-1
        #print(res1)
    if(res1==0 and path[i]=='U'):
            res2=res2+1

print(res2)
