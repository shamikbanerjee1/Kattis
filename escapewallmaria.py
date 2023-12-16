from collections import deque
def is_valid_move(final_lst, visited_tiles, curr_row,curr_col,new_row, new_col):
    if 0 <= new_row < len(final_lst) and 0 <= new_col < len(final_lst[0]) and not visited_tiles[new_row][new_col]:
        if final_lst[new_row][new_col] == '0':
            return True
        elif final_lst[new_row][new_col] == 'U':
            if new_row == curr_row+1 and new_col == curr_col:
                return True
        elif final_lst[new_row][new_col] == 'L':
            if new_row == curr_row and new_col == curr_col+1:
                return True
        elif final_lst[new_row][new_col] == 'D':
            if new_row == curr_row-1 and new_col == curr_col:
                return True
        elif final_lst[new_row][new_col] == 'R':
            if new_row == curr_row and new_col == curr_col-1:
                return True
        return False
def bfs_wallMaria(final_lst,starting_pos):
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited_tiles = [[False for _ in range(len(final_lst[0]))] for _ in range(len(final_lst))]
    queue = deque([(starting_pos[0], starting_pos[1], 0)])
    visited_tiles[starting_pos[0]][starting_pos[1]] = True
    while queue:
        current_row, current_col, distance = queue.popleft()

        if (current_row, current_col) in set_endpoints:
            lst_distance.append(distance)
            return lst_distance

        for move in possible_directions:
            new_row, new_col = current_row + move[0], current_col + move[1]

            if is_valid_move(final_lst, visited_tiles, current_row,current_col,new_row, new_col):
                visited_tiles[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

    return -1
    
t,n,m=map(int,input().split())
lst_distance=[]
final_lst=[]
start_row=0
start_col=0
set_endpoints = set()
for i in range(n):
    ip=input()
    lst=[]
    for j in range(len(ip)):
        lst.append(ip[j])
        if ip[j] == 'S':
            start_row=i
            start_col=j
    final_lst.append(lst)
for j in range(m):
    set_endpoints.add((0,j))
for j in range(n):
    set_endpoints.add((j,0))
for j in range(n):
    set_endpoints.add((j,m-1))
for j in range(m):
    set_endpoints.add((n-1,j))

time = bfs_wallMaria(final_lst,(start_row,start_col))
if time == -1:
    print('NOT POSSIBLE')
else:
    time.sort()
    if time[0] > t:
        print('NOT POSSIBLE')
    else:
        print(time[0])
