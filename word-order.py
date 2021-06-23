n=int(input())
new_list=list()
for _ in range(n):
    t=str(input())
    new_list.append(t)
new_set=set(new_list)
print(len(new_set))
new_dict=dict()
for i in new_list:
    new_dict[i]=new_dict.get(i,0)+1
print(*new_dict.values(),sep=' ')
