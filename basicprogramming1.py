n,t=map(int,input().split())
arr=list(map(int,input().split()))
if t==1:
    print(7)
elif t==2:
    print('Bigger') if arr[0]>arr[1] else print('Equal') if arr[0]==arr[1] else print('Smaller')
elif t==3:
    print(sorted(arr[:3])[1])
elif t==4:
    print(sum(arr))
elif t==5:
    print(sum(list(filter(lambda x:x%2==0,arr))))
elif t==6:
    print(''.join(map(lambda x:chr(97+(x%26)),arr)))
else:
    curr_indx=0
    next_indx=0
    dictionary={}
    dictionary[0]=1
    while True:
        next_indx=arr[curr_indx]
        if next_indx>=len(arr):
            print('Out')
            break
        elif next_indx==n-1:
            print('Done')
            break
        else:
            if dictionary.get(next_indx):
                print('Cyclic')
                break
            dictionary[next_indx]=1
            curr_indx=next_indx