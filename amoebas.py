import sys
sys.setrecursionlimit(10**6)
def dfs(i, j):
    if i < 0 or i >= len(final_lst) or j < 0 or j >= len(final_lst[0]) or final_lst[i][j] == '.':
        return
    final_lst[i][j] = '.' 
    for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1),(i+1,j+1),(i+1,j-1),(i-1,j-1),(i-1,j+1)]:
        dfs(x, y)

m,n=map(int,input().split())
final_lst=[]
for _ in range(m):
    ip = input()
    lst=[]
    for i in range(len(ip)):
        lst.append(ip[i])
    final_lst.append(lst)
components = 0
for i in range(len(final_lst)):
    for j in range(len(final_lst[0])):
        if final_lst[i][j] == '#':
            components += 1
            dfs(i, j)
print(components)
