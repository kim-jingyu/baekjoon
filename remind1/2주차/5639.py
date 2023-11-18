import sys

input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10 ** 9)
preorder_values = []

while True:
    try:
        preorder_values.append(int(input()))
    except:
        break


def solution(root_idx, end_idx):
    if root_idx > end_idx:
        return

    right_start = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if preorder_values[root_idx] < preorder_values[i]:
            right_start = i
            break

    solution(root_idx + 1, right_start - 1)
    solution(right_start, end_idx)
    print(preorder_values[root_idx])


solution(0, len(preorder_values) - 1)
