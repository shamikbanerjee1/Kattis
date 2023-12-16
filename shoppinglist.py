from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(lambda:0)
for i in range(n):
    ip=input().split()
    s = set(ip)
    for elem in s:
        dic[elem]+=1
lst=[]
for key,value in dic.items():
    if value == n:
        lst.append(key)
lst.sort()
print(len(lst))
for elem in lst:
    print(elem)