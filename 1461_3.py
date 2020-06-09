""" 1461_2과 거의 똑같은 코드 """
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))

largest = max(max(pos), -min(pos))

pos_minus, pos_plus = [], []

for i in pos:
    if i < 0:
        heapq.heappush(pos_minus, i)
    else:
        heapq.heappush(pos_plus, -i)

result = 0

while pos_plus:
    result += heapq.heappop(pos_plus)
    if pos_plus:
        heapq.heappop(pos_plus)

while pos_minus:
    result += heapq.heappop(pos_minus)
    if pos_minus:
        heapq.heappop(pos_plus)

print(-result*2-largest)