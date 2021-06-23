n=int(input())
w=len(bin(n)[2:])
for i in range(1,n+1):
    d=str(i)
    o=oct(i)
    h=hex(i)
    b=bin(i)
    print("{} {} {} {}".format(d.rjust(w,' '),o[2:].rjust(w,' '),h[2:].upper().rjust(w,' '),b[2:].rjust(w,' ')))
