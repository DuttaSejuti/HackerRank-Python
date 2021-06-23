def insertionSort1(n,arr):
    key=arr[n-1]
    for i in range(n,0,-1):
        if(i==1):
            if(arr[0]==arr[i]):
                arr[0]=key
                print(*arr)
        if(i!=1):
            if(arr[i-2]>key):
                arr[i-1]=arr[i-2]
                print(*arr)

            else:
                arr[i-1]=key
                print(*arr)
                break
n=int(input())
arr=list(map(int,input().rstrip().split()))
insertionSort1(n,arr)
# def insertionSort1(n,arr):
#     s=arr[n-1]
#     for i in range(n-2,-1,-1):
#         if(arr[i]>=s):
#             arr[i+1]=arr[i]
#             print(*arr)
#         else:
#             arr[i+1]=s
#             print(*arr)
#             break
#     else:
#         arr[i]=s
#         print(*arr)
