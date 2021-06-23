s=int(input())
new_list=list()
for _ in range(s):
    s1=str(input())
    new_list.append(s1)
for j in new_list:
    s2=str(j[0::2])
    s3=str(j[1::2])
    print("{} {}".format(s2,s3))
