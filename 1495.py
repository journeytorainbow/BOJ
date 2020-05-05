import sys

N, S, M = map(int, sys.stdin.readline().split())

# False = 0 , True = 1
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1
V = list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    for j in range(0, M+1):
        if dp[i - 1][j] == 0:
            continue
        # dp[i-1][j] != 0 인 경우,
        if j + V[i-1] <= M:
            dp[i][j + V[i-1]] = 1
        if j - V[i-1] >= 0:
            dp[i][j - V[i-1]] = 1

result = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break

print(result)

