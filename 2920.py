import sys

code = list(map(int, sys.stdin.readline().split()))

# a, d
results = [True, True]

for i in range(1, len(code)):
    if code[i] - 1 != code[i-1]:
        results[0] = False
    if code[i] + 1 != code[i-1]:
        results[1] = False

if results[0]:
    print('ascending')
elif results[1]:
    print('descending')
else:
    print('mixed')