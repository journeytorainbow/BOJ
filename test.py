""" test용 """
from collections import defaultdict
from collections import deque
import heapq

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    graph = defaultdict(dict)
    # bfs로 최단 경로에 포함된 간선들을 역추적할 때 필요
    reverse_graph = defaultdict(dict)

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        reverse_graph[v][u] = p

    print(graph)
    print(reverse_graph)