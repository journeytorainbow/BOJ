import sys

N = int(sys.stdin.readline())

cache = [0] * 10000001

cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = (cache[i-2] + cache[i-1]) % 15746

print(cache[N])


        