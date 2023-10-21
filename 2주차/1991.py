# 전위 순회 - 루트 -> 왼쪽 자식 -> 오른쪽 자식
# 중위 순회 - 왼쪽 자식 -> 루트 -> 오른쪽 자식
# 후위 순회 - 왼쪽 자식 -> 오른쪽 자식 -> 루트
import sys

N = int(sys.stdin.readline().rstrip())

graph = {}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().rstrip().split())
    graph[root] = [left, right]


def preorder_circuit(root):
    if root == '.':
        return

    print(root, end='')
    preorder_circuit(graph[root][0])
    preorder_circuit(graph[root][1])


def midorder_circuit(root):
    if root == '.':
        return

    midorder_circuit(graph[root][0])
    print(root, end='')
    midorder_circuit(graph[root][1])


def postorder_circuit(root):
    if root == '.':
        return

    postorder_circuit(graph[root][0])
    postorder_circuit(graph[root][1])
    print(root, end='')


preorder_circuit('A')
print()
midorder_circuit('A')
print()
postorder_circuit('A')
