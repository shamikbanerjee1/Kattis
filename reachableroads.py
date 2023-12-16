from collections import defaultdict
def dfs(cities_adj_lst,vertex,visited):
    if not visited[vertex]:
        visited[vertex] = True
        for adj in cities_adj_lst[vertex]:
            if not visited[adj]:
                dfs(cities_adj_lst,adj,visited)
for _ in range(int(input())):
    cities = int(input())
    visited = [False]*cities
    cities_adj_lst = defaultdict(lambda:[])
    min_paths=0
    paths = int(input())
    for _ in range(paths):
        p1,p2=map(int,input().split())
        cities_adj_lst[p1].append(p2)
        cities_adj_lst[p2].append(p1)
    for i in range(cities):
        if not visited[i]:
            dfs(cities_adj_lst,i,visited)
            min_paths+=1
            
    print(min_paths-1)