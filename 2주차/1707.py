import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

K = int(input())


def dfs(now, group):
    visited[now] = group

    for j in graph[now]:
        if not visited[j]:
            temp = dfs(j, -group)
            if not temp:
                return False
        else:
            if visited[j] == group:
                return False
    return True


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)  # 그룹이 같은지 체크

    for _ in range(E):
        V1, V2 = map(int, input().split())
        graph[V1].append(V2)
        graph[V2].append(V1)

    for i in range(1, V + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                print('NO')
                break
    else:
        print('YES')
