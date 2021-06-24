def insertionSort2(n,arr):
    for i in range(1,len(arr)):
        x=arr[i]
        j=i
        while(j>0 and arr[j-1]>x):
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=x

        print(*arr)

n=int(input())
arr=list(map(int,input().rstrip().split()))
insertionSort2(n,arr)
