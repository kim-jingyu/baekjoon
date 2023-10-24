import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

heavy_list = [[] for _ in range(N + 1)]
light_list = [[] for _ in range(N + 1)]

for _ in range(M):
    heavy, light = map(int, input().split())
    heavy_list[heavy].append(light)
    light_list[light].append(heavy)


# root 보다 가볍거나 무거운 것의 개수 구하기
def dfs(list, root):
    cnt = 0
    for node in list[root]:
        if not visited[node]:
            visited[node] = True
            cnt += 1
            cnt += dfs(list, node)
    return cnt


# 특정 구슬보다 가볍거나 무거운 구슬의 개수가 중간값 이상이면 이 구슬은 중간값이 될 수 없음
mid = (N + 1) // 2
result = 0

for root in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(heavy_list, root) >= mid:
        result += 1
    if dfs(light_list, root) >= mid:
        result += 1

print(result)