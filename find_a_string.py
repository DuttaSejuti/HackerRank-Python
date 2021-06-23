s=str(input())
sub=str(input())
count=0
s_len=len(s)
sub_len=len(sub)

for i in range(s_len):
    k=(i+sub_len)

    if(s[i:k]==sub):
        count=count+1
    i=i+1
print(count)
#print(s.count(sub))   can not count the overlapping
