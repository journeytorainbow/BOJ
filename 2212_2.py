""" 2012번과 거의 똑같은 코드 """

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

sensors = sorted(list(map(int, sys.stdin.readline().split())))

if n <= k: 
    print(0)
    sys.exit()

dist = []

for i in range(1, n):
    dist.append(sensors[i] - sensors[i-1])
dist.sort(reverse=True)

for _ in range(k-1):
    dist.pop(0)

print(sum(dist))