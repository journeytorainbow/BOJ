import sys

# 예상 등수 리스트
array = []

for _ in range(int(sys.stdin.readline())):
    array.append(int(sys.stdin.readline()))

# 오름차순으로 정렬
array.sort()

# 불만도 합 계산
result = sum(abs(index-item) for index, item in enumerate(array, start=1))
print(result)