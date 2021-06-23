
main_list=list()
for _ in range(6):
    l1=list(input().split())
    main_list.append(l1)
#print(main_list)
sum_list=list()
for i in range(0,4):
    for j in range(0,4):
        sum=int(main_list[i][j])+int(main_list[i][j+1])+int(main_list[i][j+2])+int(main_list[i+1][j+1])+int(main_list[i+2][j])+int(main_list[i+2][j+1])+int(main_list[i+2][j+2])
        sum_list.append(sum)
        j=j+1
    i=i+1
print(max(sum_list))
