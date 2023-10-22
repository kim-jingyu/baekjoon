import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    V1, V2 = map(int, input().split())
    graph[V1][V2] = graph[V2][V1] = 1

visited = [False] * (N + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        value = queue.popleft()
        for i in range(1, N + 1):
            if not visited[i] and graph[value][i]:
                visited[i] = True
                queue.append(i)


answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        answer += 1
        bfs(i)

print(answer)