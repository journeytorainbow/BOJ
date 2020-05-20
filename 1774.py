import sys
from collections import defaultdict
from math import sqrt

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(dict)
graph['edges'] = list()
parent = dict()
rank = dict()

# 인자로 두 노드의 좌표를 받음
def cal_dist(node1, node2):
    dist = sqrt((node2[1]-node1[1])**2 + (node2[0]-node1[0])**2)
    return dist

# 인자로 두 노드의 번호를 받음
def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

# 인자로 두 노드의 번호를 받음
def union(node1, node2):
    root1 = find_parent(node1)
    root2 = find_parent(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root2] == rank[root1]:
            rank[root2] += 1

# 노드 좌표 입력 받아 업데이트 하고, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().split())
    graph['nodes'][i] = (x, y)
    parent[i] = i
    rank[i] = 0 

# 간선 정보 업데이트(연결 가능한 경우 전부)
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        # 거리를 오름차순으로 정렬하기 위해 (거리, 노드, 노드)로 넣어줌
        graph['edges'].append((cal_dist(graph['nodes'][i], graph['nodes'][j]), i, j))

# 간선을 거리 기준으로 오름차순으로 정렬
graph['edges'].sort()

# 이미 연결되어 있는 노드들의 번호를 입력받아 union-find(kruskal함수 호출 전에 진행해줘야함)
for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    union(node1, node2)

result = 0
def kruskal(graph):
    global result
    for weight, node1, node2 in graph['edges']:
        if find_parent(node1) != find_parent(node2):
            union(node1, node2)
            result += weight

kruskal(graph)
print("%0.2f" % result)