def chocolateFeast(n, c, m):
    # Write your code here
    total_choco=0
    rem=int(n/c)
    total_choco=int(total_choco+rem)
    #print("Just Total choco :", total_choco)
    flag=0
    while(rem>=m):
        # total_choco=total_choco+ int(rem/m)
        # rem=int(rem/m)+(rem%m)
        if(rem%m==0):
            rem=int(rem/m)
            #print("Rem if a multiple: ",rem)
            flag=0
        else:
            rem=int((rem-1)/m)
            #print("Rem if not a multiple: ",rem)
            flag=1
        if(flag==0):
            total_choco=total_choco+rem
            #print("Total chocolate: ", total_choco)
        if(flag==1):
            total_choco=total_choco+rem
            #print("Total chocolate: ", total_choco)
            rem=rem+1

    return total_choco
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    result = chocolateFeast(n, c, m)
    print(result)


# 3       t = 3 (test cases)
# 10 2 5  n = 10, c = 2, m = 5 (first test case)
# 12 4 4  n = 12, c = 4, m = 4 (second test case)
# 6 2 2   n = 6,  c = 2, m = 2 (third test case)
#
# 6
# 3
# 5
#
# He spends 10 on 5 chocolates at 2 apiece. He then eats them and exchanges all 5 wrappers to get 1 more. He eats 6 chocolates.
