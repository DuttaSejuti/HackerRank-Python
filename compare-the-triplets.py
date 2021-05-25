def compareTriplets(a, b):
    alice_score=0
    bob_score=0
    length=3
    res=list()
    for i in range(length):
        if(a[i]>b[i]):
            alice_score=alice_score+1
        elif(a[i]<b[i]):
            bob_score=bob_score+1
        else:
            bob_score=bob_score+0
            alice_score=alice_score+0
    res.append(alice_score)
    res.append(bob_score)
    return res



a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)

print(result)
