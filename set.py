n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))

empty_s={}
empty_s=s1.union(s2)
count=0
for i in empty_s:
    count=count+1
print(count)
