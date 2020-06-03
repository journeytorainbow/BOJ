import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# 집중국 개수가 센서개수 이상 일 때, 
# 집중국을 센서 위치에 설치하면 되므로 답은 0
if k >= n:
    print(0)
    sys.exit()

# 센서 위치 오름 차순 정렬
sensors = sorted(map(int, sys.stdin.readline().split()))

# 각 센서 사이의 거리를 내림차순 정렬
distances = []
for i in range(1, len(sensors)):
    distances.append(sensors[i] - sensors[i-1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 k-1개만큼 제거
for i in range(k-1):
    distances[i] = 0

# 남은 거리들의 합이 답
print(sum(distances))