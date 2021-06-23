p=int(input())
s1=set(map(int,input().split()))
q=int(input())
s2=set(map(int,input().split()))
r1=s1.difference(s2)
r2=s2.difference(s1)
new_set=set(r1.union(r2))
new_list=list()
for i in new_set:
    new_list.append(i)
l=sorted(new_list)
for e in l:
    print(e)
