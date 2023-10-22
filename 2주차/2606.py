import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
E = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(E):
    V1, V2 = map(int, input().split())
    graph[V1][V2] = graph[V2][V1] = 1

def dfs(now):
    global answer

    for i in range(1, N + 1):
        if not visited[i] and graph[now][i]:
            visited[i] = True
            answer += 1
            dfs(i)

    return


visited[1] = True
dfs(1)
print(answer)