from collections import OrderedDict
d1={}
new_list=list()
t=int(input())
for _ in range(0,t):
    line=input()
    new_list=line.rsplit(" ",1)
    item=new_list[0]
    price=new_list[1]
    d1[item]=d1.get(item,0)+int(price)
for i,j in d1.items():
    print(i,j)





#input
#9
#BANANA FRIES 12
#POTATO CHIPS 30
#APPLE JUICE 10
#CANDY 5
#APPLE JUICE 10
#CANDY 5
#CANDY 5
#CANDY 5
#POTATO CHIPS 30

#output
#BANANA FRIES 12
#POTATO CHIPS 60
#APPLE JUICE 20
#CANDY 20
