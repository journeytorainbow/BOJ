import sys

N, M, V = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)

# 오름차순 정렬
for e in adj:
    e.sort()

#재귀 이용
def dfs(V):
    print(V, end=' ')
    visited[V] = True
    for e in adj[V]:
        if not(visited[e]):
            dfs(e)

def bfs(V):
    need_visit = list()
    need_visit.append(V)

    while need_visit:
        node = need_visit.pop(0)
        if not(visited[node]):
            visited[node] = True
            print(node, end=' ')
            """ 아래 3줄은 그냥
            need_visit.extend(adj[node])로 써줘도 상관지만,
            미리 방문한 노드인지 아닌지 확인하기 위해
            아래와 같이 써줌 """
            for e in adj[node]:
                if not(visited[e]):
                    need_visit.append(e)

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)