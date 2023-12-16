from collections import defaultdict
from queue import PriorityQueue
n,m=map(int,input().split())
bridges_lst = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    bridges_lst[a].append([b,c])
    bridges_lst[b].append([a,c])
distance = [10**9]*(n+1)
distance[1]=0
pq = PriorityQueue()
pq.put((0,1))
while not pq.empty():
    dist,vert=pq.get()
    for adj in bridges_lst[vert]:
        neighbour_dist=adj[1]
        neighbour_vert=adj[0]
        if distance[neighbour_vert] > neighbour_dist + dist:
            distance[neighbour_vert] = neighbour_dist + dist
            pq.put((distance[neighbour_vert],neighbour_vert))
print(distance[n])