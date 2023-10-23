import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
place_status = [0] + list(map(int, input()))
answer = 0

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    V1, V2 = map(int, input().split())
    graph[V1].append(V2)
    graph[V2].append(V1)
    if place_status[V1] and place_status[V2]:  # 둘 다 실내면
        answer += 2


def dfs(now, cnt):
    visited[now] = True

    for j in graph[now]:
        if place_status[j]:  # 실내면
            cnt += 1
        elif not visited[j] and not place_status[j]:  # 실외면
            cnt = dfs(j, cnt)

    return cnt


visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i] and not place_status[i]:
        result = dfs(i, 0)
        answer += result * (result - 1)

print(answer)