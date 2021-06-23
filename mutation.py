if __name__ == '__main__':
    s=input()
    n,c=input().split()
    n=int(n)
    c=str(c)
    print(s[:n]+c+s[n+1:])
