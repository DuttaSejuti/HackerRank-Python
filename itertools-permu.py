from itertools import permutations
s=list(input().split())
a=str(s[0])
b=int(s[1])
l1=permutations(a,b)
for i in sorted(l1):
    print("".join(i))
