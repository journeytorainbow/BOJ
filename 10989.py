import sys

# 계수 정렬 코드
array = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    array[int(sys.stdin.readline())] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

"""
for i in range(10001):
    print("{}\n".format(i)*array[i], end='')
"""