import sys
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, n+1)}
    distances[start] = 0
    queue = []

    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        for adj, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return distances

for _ in range(int(sys.stdin.readline())):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = defaultdict(dict)

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b][a] = s
    
    distances = dijkstra(graph, c)

    total_com = 0 
    for time in distances.values():
        if time != float('inf'):
            total_com += 1
    result_time = max(time for time in distances.values() if time != float('inf'))
    print(total_com, result_time)