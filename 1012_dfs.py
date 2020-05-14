import sys
sys.setrecursionlimit(100000)

def dfs(y, x):
    visited[y][x] = True
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if pos_list[ny][nx] and not(visited[ny][nx]):
            dfs(ny, nx) 

for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    pos_list = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    count = 0
    for pos in range(k):
        x, y = map(int, sys.stdin.readline().split())
        pos_list[y][x] = 1
    for i in range(n):
        for j in range(m):
            if pos_list[i][j] and not visited[i][j]:
                count += 1 
                dfs(i, j)
    print(count)