def divisibleSumPairs(n,k,ar):
    count=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if((ar[i]+ar[j])%k==0):
                count=count+1
    return count

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
print(result)
