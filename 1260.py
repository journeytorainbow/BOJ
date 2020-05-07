import sys
from collections import defaultdict


N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)


# 그래프 입력 받기
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start_node):
    # 내림 차순 정렬
    for key in graph.keys():
        graph[key].sort(reverse=True)

    visited = list()
    need_visit = list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    # print(*visited)
    print(' '.join(str(x) for x in visited))


def bfs(graph, start_node):
    # 오름 차순 정렬
    for key in graph.keys():
        graph[key].sort()

    visited = list()
    need_visit = list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    # print(*visited)
    print(' '.join(str(x) for x in visited))

dfs(graph, V)
bfs(graph, V)