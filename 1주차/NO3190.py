import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

L = int(input())
time_dic = {}
for i in range(L):
    X, C = input().split()
    time_dic[int(X)] = C

dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열

x, y, d = 0, 0, 0

# 뱀
snake = deque([])
time = 0
while True:
    # 뱀머리 현재 위치
    snake.append((x, y))
    time += 1

    x += dx[d]
    y += dy[d]
    if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] == 2:
        break

    if not arr[x][y]:
        i, j = snake.popleft()
        arr[i][j] = 0

    arr[x][y] = 2

    if time in time_dic:
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(time)
