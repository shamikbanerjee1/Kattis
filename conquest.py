import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def dfs(vertex,visited_islands):
    if vertex not in visited_islands:
        visited_islands.add(vertex)
        for adj in dic[vertex]:
            if army_size[-1] > dic_army[adj] and adj not in visited_islands:
                army_size.append(army_size[-1]+dic_army[adj])
                dfs(adj,visited_islands)
n,m=map(int,input().split())
dic = defaultdict(lambda :[])
dic_army = defaultdict(lambda : 0)
for _ in range(m):
    ip1,ip2=map(int,input().split())
    dic[ip1].append(ip2)
    dic[ip2].append(ip1)
for i in range(n):
    sz=int(input())
    dic_army[i+1] += sz
for i in range(n):
    if dic.get(i):
        dic[i]=sorted(dic[i], key=lambda x: dic_army[x])
visited_islands = set()
army_size = [dic_army[1]]
dfs(1,visited_islands)
print(army_size[-1])