n,m=map(int,input().split())
if (n-1) <= m <= n*(n-1)//2:
    s=set()
    lst=[]
    for i in range(1,n):
        lst.append((i,i+1))
        s.add(i+i+1)
    for i in range(1,n+1):    
        for j in range(1,n+1):
            if i!=j:
                if i+j not in s:
                    lst.append((i,j))
                    s.add(i+j)
    if len(lst)<m:
        print(-1)
    else:
        for i in range(m):
            print(str(lst[i][0])+' '+str(lst[i][1]))
else:
    print(-1)