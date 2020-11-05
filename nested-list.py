#** Find the SECOND LOWEST MARK 
#INPUT
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#OUTPUT

#Berry
#Harry




n=int(input())
new_list1=list()
d1=dict()
for i in range(n):
    s=input()
    p=float(input())
    d1.update({s:p})
#print(d1)
l=min(d1.values())
#print(l)
d2=dict()
for k,v in d1.items():
    if(v!=l):
        d2[k]=v
#print(d2)
m=min(d2.values())
#print(m)
for k in sorted(d2.keys()):
    if(d2[k]==m):
        new_list1.append(k)
new_list1.sort()
for q in new_list1:
    print(q)
