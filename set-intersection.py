t1=int(input())
s1=set(input().split())
t2=int(input())
s2=set(input().split())
s3=set()
s3=s1.intersection(s2)
print(len(s3))

#The first line contains n, the number of students who have subscribed to the English newspaper.
#The second line contains n space separated roll numbers of those students.
#The third line contains b, the number of students who have subscribed to the French newspaper.
#The fourth line contains b  space separated roll numbers of those students.
#input
#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8


#Output the total number of students who have subscriptions to both English and French newspapers.
#output
#5
