import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    V1, V2 = map(int, input().split())
    graph[V1][V2] = graph[V2][V1] = 1


def dfs(now):
    dfs_visited[now] = True
    print(now, end=' ')
    for i in range(1, N + 1):
        if not dfs_visited[i] and graph[now][i]:
            dfs(i)


def bfs(start):
    queue = deque()
    bfs_visited[start] = True
    queue.append(start)
    while queue:
        value = queue.pop()
        print(value, end=' ')
        for i in range(1, N + 1):
            if not bfs_visited[i] and graph[value][i]:
                bfs_visited[i] = True
                queue.appendleft(i)


dfs_visited = [False] * (N + 1)
dfs(V)
print()
bfs_visited = [False] * (N + 1)
bfs(V)
