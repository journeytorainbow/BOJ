import sys
import heapq

n = int(sys.stdin.readline())

assignment = []

for i in range(n):
    due, ramen = map(int, sys.stdin.readline().split())
    assignment.append((due, ramen))

# 데드라인이 오름차순으로 정렬되어야함 (컵라면수는 이후에 우선순위큐를 사용할 것이므로 지금은 순서가 어찌되도 상관x)
assignment.sort()

# 우선순위큐(최소힙)
q = []

for i in assignment:
    a = i[0]
    heapq.heappush(q, i[1])
    if a < len(q):
        heapq.heappop(q)

print(sum(q))