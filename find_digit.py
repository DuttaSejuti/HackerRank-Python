t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    main_digit=n
    while(n>0):
        digit=n%10
        if(digit!=0 and main_digit%digit==0):
            count=count+1
        n=n//10
    print(count)
