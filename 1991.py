import sys

n = int(sys.stdin.readline())

class Node:
    def __init__(self, head, left, right):
        self.head = head
        self.left = left
        self.right = right

tree = dict()

for _ in range(n):
    head, left, right = sys.stdin.readline().split()
    tree[head] = Node(head, left, right)

def pre_order(node):
    print(node.head, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])
def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.head, end='')
    if node.right != '.':
        in_order(tree[node.right])
def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.head, end='')

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])