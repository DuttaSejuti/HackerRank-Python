f_name=str(input().strip())
l_name=str(input().strip())
f_len=len(f_name)
l_len=len(l_name)
if(f_len<=10 and l_len<=10):
    print("Hello {} {}! You just delved into python.".format(f_name,l_name))
