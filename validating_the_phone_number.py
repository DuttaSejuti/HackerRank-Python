import re
n=int(input())
for _ in range(n):
    p1=input()
    l=len(p1)
    if(l==10 and p1.startswith(('7','8','9')) and p1.isdecimal()):
        print("YES")
    else:
        print("NO")
