n = int(input())
s = set(map(int, input().split()))
c=int(input())
for _ in range(0,c):
    command=input().split()
    if(command[0]=='pop'):
        s.pop()
    elif(command[0]=='remove'):
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))
print(sum(s))




#The first line contains integer n , the number of elements in the set s
#The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.

#input
#9
#1 2 3 4 5 6 7 8 9
#10
#pop
#remove 9
#discard 9
#discard 8
#remove 7
#pop
#discard 6
#remove 5
#pop
#discard 5

#Print the sum of the elements of set s on a single line.

#Output
#4
