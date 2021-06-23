from collections import defaultdict
t=list(input().split())
n=t[0]
m=t[1]
list_A=list()
list_B=list()
d1=defaultdict(list)
for _ in range(int(n)):
    s1=str(input())
    list_A.append(s1)
for _ in range(int(m)):
    s2=str(input())
    list_B.append(s2)
for i in range(0,int(n)):
    d1[list_A[i]].append(i+1)
key=d1.keys()
#print(d1)
for p in list_B:
    for k,v in d1.items():
        if (p==k):
            print(*v)
    if(p not in key):
        print('-1')



#In this challenge, you will be given 2 integers,m  and n. There are n words, which might repeat, in word group A.
# There are m words belonging to word group B. For each m words, check whether the word has appeared in group  A
# or not. Print the indices of each occurrence of m  in group . If it does not appear, print -1.

#The first line contains integers,m and n separated by a space.
#The next  lines contains the words belonging to group A.
#The next  lines contains the words belonging to group B.


##input
#5 2
#a
#a
#b
#a
#b
#a
#b

#output
#1 2 4
#3 5
