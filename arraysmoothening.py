import heapq
n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
dic={}
for elem in arr:
    if dic.get(elem):
        dic[elem]+=1
    else:
        dic[elem]=1
if k == 0:
    max_value=-1
    for key,value in dic.items():
        if max_value<value:
            max_value=value
    print(max_value)
else:
    min_to_max_heap=[]
    lst=list(dic.values())
    lst.sort(reverse=True)
    for i in range(len(lst)):
        lst[i]*=-1
    for elem in lst:
        heapq.heappush(min_to_max_heap,elem)
    while k!=0:
        popped_value=heapq.heappop(min_to_max_heap)
        popped_value-=-1
        heapq.heappush(min_to_max_heap,popped_value)
        k-=1
    print(abs(heapq.heappop(min_to_max_heap)))