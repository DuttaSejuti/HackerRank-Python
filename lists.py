n=int(input())
new_list1=list()
res_list=list()
for _ in range(n):
    c=input()
    new_list1=c.split()
    if(new_list1[0]=='insert'):
        res_list.insert(int(new_list1[1]),int(new_list1[2]))
    elif(new_list1[0]=='print'):
        print(res_list)
    elif(new_list1[0]=='remove'):
        res_list.remove(int(new_list1[1]))
    elif(new_list1[0]=='append'):
        res_list.append(int(new_list1[1]))
    elif(new_list1[0]=='pop'):
        res_list.pop()
    elif(new_list1[0]=='reverse'):
        res_list.reverse()
    else:
        res_list.sort()




#l = list()
#for _ in range(int(input()))
#    cmd,*args=input().split()
#    if cmd=='print':
#        print(l)
#    else:
#        getattr(l,cmd)(*list(map(int,args)))
