from itertools import product
a=set(map(int,input().split()))
b=set(map(int,input().split()))
l=list(product(a,b))
print(*l)
