""" Python3로 제출 시 시간초과 / PyPy3로 제출해야 통과 가능
while문 코드가 달라지면 PyPy3로도 통과 불가능한 경우가 있음 """

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# 컴퓨터 연결 정보
com = [[] for i in range(n+1)]

# 각 컴퓨터별로 연결관계 업데이트 
for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    com[x].append(y)

def bfs(start_node):
    count = 1
    need_visit = deque([start_node])
    visited = [False]*(n+1)
    visited[start_node] = True

    while need_visit:
        node = need_visit.popleft()
        for e in com[node]:
            if not(visited[e]):
                need_visit.append(e)
                visited[e] = True
                count += 1
    return count 

result = []
max_value = -1
for i in range(1, n+1):
        temp = bfs(i)
        if temp > max_value:
            result = [i]
            max_value = temp
        elif temp == max_value:
            result.append(i)
            max_value = temp

for e in result:
    print(e, end=" ")