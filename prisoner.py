n=int(input())
sum_count=0
new_list1=list()
for i in range(n):
    arr=list(map(int,input().rstrip().split()))
    n=arr[0]
    m=arr[1]
    s=arr[2]
    new_list1.append(s)
    len_list=len(new_list1)
    if(len_list==m):
        print(new_list1[-1])
    else:
        for i in range(m-1):
            if(s<n):
                s=s+1
                new_list1.append(s)
            else:
                s=0
                s=s+1
                new_list1.append(s)
        new_list1.reverse()
        print(new_list1[0])
