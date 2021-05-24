def cutTheSticks(arr):
    res=list()
    l=len(arr)
    res.append(l)
    arr.sort()
    min_element=min(arr)
    #print("Sorted list:",arr)
    while(l>1):
        for i in range(l):
            arr[i]=abs(arr[i]-min_element)
        print("After subtracting:",arr)
        min_element=min(arr)
        min_occ=arr.count(min_element)
        print('{} has occurred {} times'.format(min_element, min_occ))
        if(min_occ==l):
            break
        del arr[0:min_occ]
        print("After eleminating the min elements",arr)
        l=len(arr)
        res.append(l)
        print("the result:",res)
    return res
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print(result)


# Sample input
# 8
# 1 2 3 4 3 3 2 1
# Sample Output 
# 8
# 6
# 4
# 1
#
# sticks-length         length-of-cut   sticks-cut
# 1 2 3 4 3 3 2 1         1               8
# _ 1 2 3 2 2 1 _         1               6
# _ _ 1 2 1 1 _ _         1               4
# _ _ _ 1 _ _ _ _         1               1
# _ _ _ _ _ _ _ _       DONE            DONE













n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print(result)
