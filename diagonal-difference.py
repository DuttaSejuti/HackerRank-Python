def diagonalDifference(arr):
    # Write your code here
    diff=0
    diagonal_1=0
    diagonal_2=0
    length=len(arr)
    l=length
    for i in range(length):
        for j in range(length):
            if(i==j):
                diagonal_1=diagonal_1+arr[i][j]

        for k in reversed(range(length)):
            if(k==(l-1)):
                diagonal_2=diagonal_2+arr[i][k]
        l=l-1
    diff=abs(diagonal_1-diagonal_2)

    return diff


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)

# 3
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal =1+5+9=15 . The right to left diagonal =3+5+9=17 . Their absolute difference is |15-17|=2.
