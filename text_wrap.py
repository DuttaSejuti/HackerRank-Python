s=str(input())
l=len(s)
w=int(input())
lst=list()
while(l>0):
    lst.append(s[:w])
    s=s[w:]
    l=len(s)
print(*lst,sep='\n')


#input
#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4

#output
#ABCD
#EFGH
#IJKL
#IMNO
#QRST
#UVWX
#YZ
