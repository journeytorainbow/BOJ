""" 우선순위큐 사용 O """

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
pos_books = list(map(int, sys.stdin.readline().split()))

# 원점에서 가장 멀리있는 좌표까지의 거리
largest = max(max(pos_books), -min(pos_books))

# 양수 좌표들
pos_plus = []
# 음수 좌표들
pos_minus = []

# heapq를 최대힙(max heap)을 사용하기 위해 좌표들을 음수로 바꾼다
for i in pos_books:
    if i > 0:
        heapq.heappush(pos_plus, -i)
    else:
        heapq.heappush(pos_minus, i)

result = 0

while pos_plus:
    result += heapq.heappop(pos_plus)
    for _ in range(m - 1):
        if pos_plus:
            heapq.heappop(pos_plus)

while pos_minus:
    result += heapq.heappop(pos_minus)
    for _ in range(m - 1):
        if pos_minus:
            heapq.heappop(pos_minus)

# 가장 먼 곳은 마지막에 방문하므로 
# 가장 먼 곳에 한해서 편도 거리만 계산
print(-result * 2 - largest)