n=int(input())
arr=list(map(int,input().split()))
arr.sort()
total=arr[0]
for i in range(1,n):
    if arr[i]-1 != arr[i-1]:
        total+=arr[i]
print(total)