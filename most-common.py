from collections import Counter
logo=str(input().strip())
k=Counter(sorted(logo)).most_common(3)
#print(com_dic)
#print(type(k))
for i,j in k:
    print(i,j)
