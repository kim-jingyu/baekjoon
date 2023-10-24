import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1


bfs(0, 0)

print(graph[N - 1][M - 1])
