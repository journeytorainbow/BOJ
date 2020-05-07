import sys
from collections import deque

# 수빈의 위치=start_pos, 동생의 위치
N, K = map(int, sys.stdin.readline().split())
# 이동할 수 있는 점은 0부터 10만까지
array = [0] * 100001

def bfs(start_pos):
    # 큐는 그냥 일반 리스트로 구현해도 상관없음
    need_visit = deque([start_pos])

    while need_visit:
        now_pos = need_visit.popleft()
        if now_pos == K:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos <= 100000 and not(array[next_pos]):
                array[next_pos] = array[now_pos] + 1
                need_visit.append(next_pos)
print(bfs(N))