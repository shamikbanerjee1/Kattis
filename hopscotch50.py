import heapq
from collections import defaultdict

m,k=map(int,input().split())
final_lst=[]
coordinates_dictionary=defaultdict(list)
distances = [[10**9]*m for _ in range(m)]
for _ in range(m):
    ip = list(map(int,input().split()))
    final_lst.append(ip)
for i in range(m):
    for j in range(m):
        coordinates_dictionary[final_lst[i][j]].append((i,j))
all_one_coordinates = coordinates_dictionary[1]
for i in range(len(all_one_coordinates)):
    distances[all_one_coordinates[i][0]][all_one_coordinates[i][1]]=0
min_distance_arr=[]
for i in range(len(all_one_coordinates)):
   heapq.heappush(min_distance_arr, (1,0,all_one_coordinates[i]))
min_dist=10**9
reach_k=True
while len(min_distance_arr) != 0:
    get_info=heapq.heappop(min_distance_arr)
    vertex=get_info[0]
    dist=get_info[1]
    coordinates=get_info[2]
    if vertex == k:
        min_dist=dist
        break
    if coordinates_dictionary.get(vertex+1):
        lst_neighbours = coordinates_dictionary[vertex+1]
        for adj_neighbour in lst_neighbours:
            manhattan_distance = abs(coordinates[0]-adj_neighbour[0]) + abs(coordinates[1]-adj_neighbour[1])
            if (distances[adj_neighbour[0]][adj_neighbour[1]] > manhattan_distance + distances[coordinates[0]][coordinates[1]]):
                distances[adj_neighbour[0]][adj_neighbour[1]] = manhattan_distance + distances[coordinates[0]][coordinates[1]]
                heapq.heappush(min_distance_arr,(vertex+1,distances[adj_neighbour[0]][adj_neighbour[1]],adj_neighbour))
    else:
        reach_k=False
        break
if reach_k:
    print(min_dist)
else:
    print(-1)
        