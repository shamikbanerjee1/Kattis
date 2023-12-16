arr=input().split()
is_sorted=False
swaps=0
for _ in range(len(arr)):
    if is_sorted:
        break
    else:
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                print(*arr)
                swaps+=1
        if swaps==0:
            is_sorted=True
        else:
            swaps=0
            