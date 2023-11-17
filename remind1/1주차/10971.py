import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9
visited = [False] * N
temp = []


def solution(level, start, current):
    global answer
    if level == N - 1 and W[current][start]:
        temp.append(W[current][start])
        answer = min(answer, sum(temp))
        temp.pop()
        return

    for target in range(N):
        if not visited[target] and W[current][target] and answer > sum(temp):
            visited[target] = True
            temp.append(W[current][target])
            solution(level + 1, start, target)
            visited[target] = False
            temp.pop()


for i in range(N):
    visited[i] = True
    solution(0, i, i)
    visited[i] = False

print(answer)