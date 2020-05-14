""" 답은 올바르게 출력되나, 시간초과 뜬 코드 ㅠㅠ """

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# 컴퓨터 연결 정보
com = [[] for i in range(n+1)]
# 진입차수
indegree = [0] * (n+1)

# 각 번호별로 노드 연결관계/진입차수 업데이트
for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    com[x].append(y)
    indegree[y] += 1

def bfs(start_node):
    count = 0
    need_visit = deque([start_node])
    visited = [False]*(n+1)

    while need_visit:
        node = need_visit.popleft()
        if not(visited[node]):
            visited[node] = True
            count += 1
            need_visit.extend(com[node]) 
    return count 

result = []
max_value = -1

for i in range(1, n+1):
    if indegree[i] == 0:
        temp = bfs(i)
        if temp > max_value:
            result = [i]
            max_value = temp
        elif temp == max_value:
            result.append(i)
            max_value = temp

for e in result:
    print(e, end=" ")