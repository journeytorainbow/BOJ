import sys
from collections import deque

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

adj = [[] for _ in range(node+1)]

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs():
    count = 0
    # start_node = 1로 항상 동일
    need_visit = deque([1])
    
    while need_visit:
        node = need_visit.popleft()
        if not(visited[node]):
            visited[node] = True
            count += 1
            for e in adj[node]:
                if not(visited[e]):
                    need_visit.append(e)
    return count-1

visited = [False]*(node+1)
print(bfs())