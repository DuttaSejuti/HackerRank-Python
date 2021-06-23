import string

l1="abcdefghijklmnopqrstuvwxyz"
size=int(input())
sub=l1[:size]
#print(sub)
base='-'.join(reversed(sub))
print(base)
