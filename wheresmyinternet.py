from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def dfs(starting_vertex,lst_pairs):
    if starting_vertex not in visited_houses:
        visited_houses.add(starting_vertex)
        if bool_house[starting_vertex]:
            for adj in lst_pairs[starting_vertex]:
                bool_house[adj]=True
                dfs(adj,lst_pairs)
            
n,m=map(int,input().split())
lst_pairs=defaultdict(lambda:[])
for _ in range(m):
    h1,h2=map(int,input().split())
    lst_pairs[h1].append(h2)
    lst_pairs[h2].append(h1)
visited_houses=set()
bool_house = [False]*(n+1)
if not lst_pairs.get(1):
    for i in range(2,n+1):
        print(i)
else:
    bool_house[1]=True
    for i in range(1,n+1):
        dfs(i,lst_pairs)
    if all (bool_house[1:]):
        print('Connected')
    else:
        for i in range(2,n+1):
            if not bool_house[i]:
                print(i)