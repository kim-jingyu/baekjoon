import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

bottom = 0
up = max(trees)
answer = 0

while bottom <= up:
    mid = (bottom + up) // 2
    total = 0

    for tree in trees:
        if tree >= mid:
            total += (tree - mid)

    if total >= M:
        bottom = mid + 1
    else:
        up = mid - 1

print(up)
