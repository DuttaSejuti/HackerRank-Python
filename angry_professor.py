n=int(input())
for _ in range(n):
    n,k=input().split()
    new_list=list(map(int,input().rstrip().split()))
    count=0
    for element in new_list:
        if(element<=0):
            count=count+1

    if(count>=k):
        print("NO")
    else:
        print("YES")
