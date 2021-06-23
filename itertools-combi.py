# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s=list(input().split())
a=str(s[0])
b=int(s[1])
for i in range(1,b+1):
    l1=combinations(sorted(a),i)
    for j in l1:
        print("".join(j))


#You are given a string S
#Your task is to print all possible combinations, up to size k  of the string in lexicographic sorted order.

#input
#HACK 2

#output
#A
#C
#H
#K
#AC
#AH
#AK
#CH
#CK
#HK
