n=int(input().strip())
if(n>=1 and n<=100):
    a=n%2
    if(a!=0):
        print("Weird")
    elif (a==0):
        if(n>=2 and n<=5):
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
