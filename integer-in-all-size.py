a=int(input())
b=int(input())
c=int(input())
d=int(input())
n=1
for _ in range(0,b):
    n=a*n
m=1
for _ in range(0,d):
    m=c*m
print(n+m)
#print(pow(a,b)+pow(c,d))
