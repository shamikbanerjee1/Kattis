from collections import defaultdict
from queue import PriorityQueue
import sys
while True:
    n,m,q,s=map(int,sys.stdin.readline().split())
    edge_weights=defaultdict(list)
    if not n and not m and not q and not s:
        break
    for _ in range(m):
        v1,v2,w=map(int,sys.stdin.readline().split())
        edge_weights[v1].append([v2,w])
    query_lst=[]
    for _ in range(q):
        vertex=sys.stdin.readline()
        query_lst.append(int(vertex))
    distance_arr=[10**9]*n
    distance_arr[s]=0
    pq=PriorityQueue()
    pq.put((0,s))
    while not pq.empty():
        dist,vert=pq.get()
        for adj in edge_weights[vert]:
            neighbour_dist=adj[1]
            neighbour_vert=adj[0]
            if distance_arr[neighbour_vert] > neighbour_dist + dist:
                distance_arr[neighbour_vert] = neighbour_dist + dist
                pq.put((distance_arr[neighbour_vert],neighbour_vert))
    for query in query_lst:
        if distance_arr[query] == 10**9:
            print('Impossible')
        else:
            print(distance_arr[query])
    print()