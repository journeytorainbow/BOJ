import sys
from collections import deque

def bfs(y, x):
    need_visit = deque([(y,x)])
    visited[y][x] = 1

    while need_visit:
        y, x = need_visit.popleft()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if pos_list[ny][nx] and not(visited[ny][nx]):
                need_visit.append((ny, nx))
                visited[ny][nx] = True

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
            if pos_list[i][j] and not(visited[i][j]):
                count += 1
                bfs(i, j)
    print(count)
