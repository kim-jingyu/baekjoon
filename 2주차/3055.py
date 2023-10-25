import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
water = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            x1, y1 = i, j
            graph[i][j] = '.'
        elif graph[i][j] == '*':
            water.append([i, j])


# 홍수
def flood():
    water_length = len(water)

    while water_length:
        x, y = water.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    water.append([nx, ny])

        water_length -= 1


# 고슴도치 이동
def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        q_length = len(queue)

        while q_length:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])

                    elif graph[nx][ny] == 'D':
                        print(visited[x][y])
                        return
            q_length -= 1
        flood()

    print("KAKTUS")
    return


flood()
bfs(x1, y1)
