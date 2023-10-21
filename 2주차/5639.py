import sys

sys.setrecursionlimit(10 ** 9)
preorder_values = []

graph = []

while True:
    try:
        preorder_values.append(int(sys.stdin.readline().rstrip()))
    except:
        break


def preorder_to_postgraph(root, end):
    if root > end:
        return

    # 오른쪽 노드가 없으면
    right_start = end + 1

    # 오른쪽 노드가 있으면
    for i in range(root + 1, end + 1):
        if preorder_values[i] > preorder_values[root]:
            right_start = i
            break

    preorder_to_postgraph(root + 1, right_start - 1)
    preorder_to_postgraph(right_start, end)
    graph.append(preorder_values[root])


preorder_to_postgraph(0, len(preorder_values) - 1)
for i in graph:
    print(i)
