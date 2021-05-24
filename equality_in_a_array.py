n=int(input())
arr=list(map(int,input().rstrip().split()))
count=0
new_set=set()
count_list=list()
for i in arr:
    new_set.add(i)
for k in new_set:
    for m in arr:
        if(m!=k):
            count=count+1
    count_list.append(count)
    count=0
print(min(count_list))

#(the below one is for more complicated cases...like if i want same length same element list...(3,3,3) (4,4,4,4))

#new_dict=dict()
#new_list1=list() #wanted
#new_list2=list() #unwanted
#count=0
#count_list=list()
#for i in arr:
#    new_dict[i]=new_dict.get(i,0)+1
#print(new_dict.items())
#for k,v in new_dict.items():
#    if(k==v):
#        new_list1.append(k)
#    else:
#        new_list2.append(k)
#s=len(new_list1)
#for r in range(s):
#    for m in arr:
#        if(new_list1[r]!=m):
#            count=count+1
#    count_list.append(count)
#    count=0

#print(min(count_list))
