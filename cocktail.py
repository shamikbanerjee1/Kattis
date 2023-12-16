n,t=map(int,input().split())
arr=sorted([int(input())for i in range(n)],reverse=True)
flag=True
for i in range(1,n):
    for j in range(0,i):
        arr[j] -= t
    if not all(arr[0:i]):
        flag=False
        break
if flag:
    print('YES')
else:
    print('NO')