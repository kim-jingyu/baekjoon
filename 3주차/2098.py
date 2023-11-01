import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dp = {}


def dfs(now, visited):
    if visited == (1 << N) - 1:
        if board[now][0]:
            return board[now][0]
        else:
            # 출발점으로 갈 수 없는 경우
            return int(1e9)

    if (now, visited) in dp:
        return dp[(now, visited)]

    min_cost = int(1e9)
    for next in range(1, N):
        if not board[now][next] or visited & (1 << next):  # 이미 방문한 경로면 무시
            continue
        cost = dfs(next, visited | (1 << next)) + board[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost


print(dfs(0, 1))
