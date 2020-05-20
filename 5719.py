import sys
import heapq
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

def dijkstra():
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        for adj, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adj] and not dropped[current_node][adj]:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])

# 최단 경로들에 포함된 간선들을 탐색하고 제외해주기 위해 bfs를 사용
def bfs():
    queue = deque()
    queue.append(end)
    while queue:
        current_node = queue.popleft()
        if current_node == start:
            continue
        for prev, weight in reverse_graph[current_node].items():
            if distances[current_node] == distances[prev] + weight:
                dropped[prev][current_node] = True
                queue.append(prev)

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
    dropped = [[False]*(n) for _ in range(n)] # 최단 경로에 포함되는 간선들에 대해 True로 업데이트 할 예정
    distances = {node: float('inf') for node in range(0, n)}
    dijkstra() # 1 최단 경로 탐색
    bfs() # 1에서 업데이트된 distances와 reverse_graph 이용해 역추적하여 최단 경로에 포함된 간선 탐색(dropped가 업데이트됨)
    distances = {node: float('inf') for node in range(0, n)} # 초기화
    dijkstra() # 2 최단 경로를 이루는 간선들을 제외한 간선들에 대해 최단 경로 탐색 (거의 최단 경로 탐색)
    if distances[end] != float('inf'):
        print(distances[end])
    else:
        print(-1)