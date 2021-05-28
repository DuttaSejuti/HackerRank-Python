def miniMaxSum(arr):
    # Write your code here
    res=list()
    res.append(sum(arr[1:5]))
    res.append(arr[0]+sum(arr[2:5]))
    res.append(sum(arr[0:2])+sum(arr[3:5]))
    res.append(sum(arr[0:3])+arr[4])
    res.append(sum(arr[0:4]))
    res.sort()
    print(res[0],res[4])

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
