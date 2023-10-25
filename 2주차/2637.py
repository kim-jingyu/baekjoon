import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

edges = [[] for _ in range(N + 1)]
need = [0] * (N + 1)
answer = [0] * (N + 1)
answer[N] = 1

for _ in range(M):
    X, Y, K = map(int, input().split())
    edges[X].append([Y, K])
    need[Y] += 1

queue = deque([N])
atom = [i for i in range(1, N + 1) if not edges[i]]

while queue:
    now = queue.popleft()
    for next, cnt in edges[now]:
        need[next] -= 1
        answer[next] += cnt * answer[now]
        if not need[next]:
            queue.append(next)


for i in atom:
    print(i, answer[i])
