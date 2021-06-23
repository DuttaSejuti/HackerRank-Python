n=int(input())
student_marks={}
for _ in range(n):
    name,*line=input().split()
    scores=list(map(float, line))
    student_marks[name]=scores
#print(student_marks)
query_name=str(input())
for i in student_marks:
    if(query_name==i):
        a=sum(student_marks[i])
        res=float(a/3)
        print("%.2f" % res)
        #res=float(sum(scores)/3)
        #print("%.2f" % res)
