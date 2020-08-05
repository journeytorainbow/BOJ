import sys, heapq

n, m = map(int, sys.stdin.readline().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    result.append(node)
    if array[node]:
        for i in array[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)

for i in result:
    print(i, end=' ')