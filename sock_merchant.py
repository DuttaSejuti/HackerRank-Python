n = int(input())
ar = list(map(int, input().rstrip().split()))
new_dict=dict()

for i in ar:
    new_dict[i]=new_dict.get(i,0)+1
#print(*new_dict.values(),sep=' ')
pair=0

for key in new_dict:
    v=new_dict[key]/2
    pair=pair+int(v)
print(pair)
