import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline(). split()))

sum_cards = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= m and sum_cards < temp:
                sum_cards = temp

print(sum_cards)