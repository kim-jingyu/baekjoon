import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    V1, V2 = map(int, input().split())
    graph[V1].append(V2)
    graph[V2].append(V1)


def dfs(now):
    for j in graph[now]:
        if visited[j] == 0:
            visited[j] = now
            dfs(j)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = start
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if visited[i] == 0:
                visited[i] = value
                queue.append(i)


bfs(1)

for i in range(2, N + 1):
    print(visited[i])
