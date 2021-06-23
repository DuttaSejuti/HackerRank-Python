from collections import deque
d = deque()
t=int(input())
for _ in range(0,t):
    command=input().split()
    if(command[0]=='append'):
        d.append(int(command[1]))
    elif(command[0]=='appendleft'):
        d.appendleft(int(command[1]))
    elif(command[0]=='popleft'):
        d.popleft()
    else:
        d.pop()

print(*d,sep=' ')




#The first line contains an integer N, the number of operations.
#The next N lines contains the  space separated names of methods and their values.

#input
#6
#append 1
#append 2
#append 3
#appendleft 4
#pop
#popleft

#Print the space separated elements of deque d.

#Output
#1 2
