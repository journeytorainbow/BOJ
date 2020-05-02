import sys


# 노드 생성
class Node:
    def __init__(self, node_num, left_node, right_node):
        
        self.parent = -1
        self.node_num = node_num
        self.left_node = left_node
        self.right_node = right_node

# 중위 순회
def in_order(node, level):
    global level_depth, x
    # 트리의 최대 depth를 구하기 위함
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level+1)
    # 현재 레벨에서 가장 왼/오른쪽의 열 번호를 각각 기록할 수 있도록 한다
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    # x축(열)으로 1씩 증가
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level+1)

# 노드 개수 입력받기
N = int(sys.stdin.readline())

# 트리는 딕셔너리 이용
tree = {}
# 인덱스 맞춰주기 (level은 1부터 시작하니까)
# 아래 두 변수에는 각 레벨(행)별로 가장 왼/오른쪽의 열번호가 기록됨
level_min = [N]
level_max = [1]


# 초기값들
# 루트 노드를 찾아서 그 노드 번호를 기록하기 위한 변수
root = -1 
# 열번호
x = 1 
# 트리의 depth
level_depth =1

# 트리 초기화
for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(N)
    level_max.append(0)

# 트리 정보 입력받아서 트리 업데이트
for _ in range(N):
    node_num, left_node, right_node = map(int, sys.stdin.readline().split())
    tree[node_num].left_node = left_node
    tree[node_num].right_node = right_node
   
# 부모 노드 기록
    if left_node != -1:
        tree[left_node].parent = node_num
    if right_node != -1:   
        tree[right_node].parent = node_num

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i

# 중위 순회 함수 호출
in_order(tree[root], 1)


# 정답 구하기 위한 코드
result_level = 1
result_width = level_max[1] - level_min[1] + 1

for i in range(2, level_depth+1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
    
print(result_level, result_width)