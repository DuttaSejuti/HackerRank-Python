lst1=list(input().split())
lst2=list(input().split())
d1=int(lst1[0])
m1=int(lst1[1])
y1=int(lst1[2])
d2=int(lst2[0])
m2=int(lst2[1])
y2=int(lst2[2])
if((d1>=d2 or d1<=d2) and (m1<=m2 or m1>=m2) and y1>y2):
    total_fine=10000
    print(int(total_fine))
elif(d1>d2 and  m1==m2 and y1==y2):
    total_fine=15*(d1-d2)
    print(total_fine)
elif(d1>=d2 and m1>m2 and y1==y2):
    total_fine=500*(m1-m2)
    print(int(total_fine))
else:
    total_fine=0
    print(int(total_fine))
