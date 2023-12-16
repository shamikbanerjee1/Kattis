for _ in range(int(input())):
    ip=list(map(int,input().split()))
    k=ip[0]
    arr=ip[1:]
    swaps=0
    for i in range(1,len(arr)):
        value = arr[i]
        value_index = i - 1
        while value_index>=0 and value<arr[value_index]:
            arr[value_index+1]=arr[value_index]
            value_index-=1
            swaps+=1
        arr[value_index+1]=value
    print(k,swaps)