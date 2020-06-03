""" 우선순위큐 사용 X """

import sys

n, m = map(int, sys.stdin.readline().split())
pos_books = list(map(int, sys.stdin.readline().split()))

pos_minus = []
pos_plus = []

for i in pos_books:
    if i < 0:
        pos_minus.append(-i)
    else:
        pos_plus.append(i)

# 내림차순 정렬
pos_minus.sort(reverse=True)
pos_plus.sort(reverse=True)

result = 0

i = 0
while i < len(pos_minus):
    result += pos_minus[i]*2
    i += m

i = 0
while i < len(pos_plus):
    result += pos_plus[i]*2
    i += m 

result -= max(pos_minus[0], pos_plus[0])
print(result)