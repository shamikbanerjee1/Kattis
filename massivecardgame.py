def find_lower_ele(arr,ele,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>=ele:
            high=mid-1
        else:
            low=mid+1
    return high
    
def find_higher_ele(arr,ele,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]<=ele:
            low=mid+1
        else:
            high=mid-1
    return low
n=int(input())
arr=sorted(list(map(int,input().split())))
for _ in range(int(input())):
    l,r=map(int,input().split())
    find_lower_element=find_lower_ele(arr,l,0,n-1)
    find_higher_element=find_higher_ele(arr,r,0,n-1)
    
    print(find_higher_element-find_lower_element-1)    