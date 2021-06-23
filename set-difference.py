def set_difference(a,b):
    c= a.difference(b)
    l=len(c)

    return l
t1= int(input())
a= set(map(int, input().rstrip().split()))
t2= int(input())
b= set(map(int, input().rstrip().split()))
result=set_difference(a,b)
print(result)
