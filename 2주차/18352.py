import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                queue.append(next)


bfs(X)

if K in distance:
    for i in range(1, N + 1):
        if distance[i] == K:
            print(i)
else:
    print(-1)