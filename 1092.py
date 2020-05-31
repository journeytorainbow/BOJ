import sys

n = int(sys.stdin.readline())
cranes = sorted(map(int, sys.stdin.readline().split()), reverse=True)

m = int(sys.stdin.readline())
boxes = sorted(map(int, sys.stdin.readline().split()), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

# 각 크레인이 현재 옮겨야 하는 박스의 번호(크레인, 박스 모두 0번 부터 시작)
positions = [0] * n
# 각 박스가 이미 배로 옮겨졌는지 아닌지 체크
checked = [False] * m

count = 0
result = 0

while True:
    # 박스를 모두 실었다면 종료
    if count == len(boxes):
        break

    # 아래 반복문 종료 = 1분 지남
    for i in range(n): # 매 분마다 모든 크레인을 확인
        while positions[i] < len(boxes): 
            # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날 때 까지 반복
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1 
print(result)