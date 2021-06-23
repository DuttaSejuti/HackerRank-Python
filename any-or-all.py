n=int(input())
lst=list(input().split())
for i in lst:
    temp=i
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if(i>0 and temp==rev):
    print('True')
else:
    print('False')
