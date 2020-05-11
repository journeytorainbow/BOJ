import sys

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

adj = [[] for i in range(node+1)]

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

count = 0 
def dfs(start_node):
    global count
    count += 1 
    visited[start_node] = True
    for next_node in adj[start_node]:
        if not(visited[next_node]):
            dfs(next_node)
    return count-1

visited = [False]*(node+1)
print(dfs(1))