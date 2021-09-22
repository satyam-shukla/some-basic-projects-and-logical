n=0
x=0
for i in range(999,100,-1):
    for j in range(999,100,-1): 
        s=str(i*j)
        if s==s[::-1]:
            if x<int(s):
                x=int(s)
                print(s)

