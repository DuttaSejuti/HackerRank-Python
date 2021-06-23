from collections import Counter
d1={}
total_money=0
shoe=int(input())
size=list(map(int,input().split()))
for n in size:
    d1[n]=d1.get(n,0)+1
#d1=Counter(size).items()
print(d1)
#key_list=d1.keys()
#val_list=d1.values()
cus=int(input())
for _ in range(cus):
    s,x=map(int,input().split())
    if(s in d1.keys()):
        if(d1[s]>0):
            total_money=total_money+x
            d1[s]=d1[s]-1
print(d1)
            #d1[i]=d1.setdefault(i,0)-1
print(total_money)
