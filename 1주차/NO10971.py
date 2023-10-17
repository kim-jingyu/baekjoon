import sys

N = int(sys.stdin.readline().rstrip())

board = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N))
visited = [False] * N
answer = 1e9


def solution(level, temp, now, start):
    global answer
    if level == N-1 and board[now][start]:
        temp += board[now][start]
        answer = min(answer, temp)
        return

    for i in range(N):
        if not visited[i] and board[now][i] and temp < answer:
            visited[i] = True
            solution(level + 1, temp + board[now][i], i, start)
            visited[i] = False


for i in range(N):
    visited[i] = True
    solution(0, 0, i, i)
    visited[i] = False


print(answer)
