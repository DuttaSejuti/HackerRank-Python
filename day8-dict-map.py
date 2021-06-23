t=int(input())
d1=dict(input().split() for _ in range(t))
#print(d1)
lst1=d1.keys()
lst2=d1.values()
while True:
    try:
        n=str(input())
        if(n in lst1):
            print("{}={}".format(n,d1[n]))
        else:
            print("Not found")
    except:
        break
