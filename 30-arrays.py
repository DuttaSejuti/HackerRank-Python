n=int(input())
lst=list(map(int,input().split()))
i=n-1
new_list=list()
while i>-1:
    new_list.append(lst[i])
    i=i-1
print(*new_list)

#while true:
#    print(lst[i])
