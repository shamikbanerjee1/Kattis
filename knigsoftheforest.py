import heapq
k,n=map(int,input().split())
entry_yr,strength=map(int,input().split())
lst=[(entry_yr,-strength)]
for _ in range(n+k-2):
    en,st=map(int,input().split())
    lst.append((en,-st))
heapq.heapify(lst)
lst_strength=[]
while k!=0:
    popped_ele=heapq.heappop(lst)
    heapq.heappush(lst_strength,(popped_ele[1],popped_ele[0]))
    k-=1
present_year=lst_strength[0][1]
winning_yr=None
while lst:
    if lst_strength[0][0] == -strength:
        winning_yr=present_year
        break
    else:
        heapq.heappop(lst_strength)
        heapq.heappush(lst_strength,(lst[0][1],lst[0][0]))
        heapq.heappop(lst)
        present_year+=1
if winning_yr==None:
    if lst_strength[0][0] == -strength:
        print(present_year)
    else:
        print('unknown')
else:
    print(present_year)