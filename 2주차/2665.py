import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    visited[0][0] = 1

    while q:
        answer, y, x = heapq.heappop(q)

        if y == n - 1 and x == n - 1:
            print(answer)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if graph[ny][nx] == 0:
                    heapq.heappush(q, [answer + 1, ny, nx])
                else:
                    heapq.heappush(q, [answer, ny, nx])


dijkstra()