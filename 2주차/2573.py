import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())  # 행, 열
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
year = 0


# 빙산의 위치 i, j를 받아와서 빙산 주변 바다 갯수 카운트
def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                # 빙산이라면 큐에 추가
                if board[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                # 빙산이 아니라면 바닷물로 카운트
                else:
                    cnt[y][x] += 1

    return 1


while True:
    answer = []
    visited = [[False] * M for _ in range(N)]
    cnt = [[0] * M for _ in range(N)]

    # 빙산과 접촉되어 있는 바닷물 확인
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                answer.append(bfs(i, j))

    # 빙산 깍아주기
    for i in range(N):
        for j in range(M):
            board[i][j] -= cnt[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    # 빙산 그룹이 없거나 2 덩어리 이상이라면
    if len(answer) == 0 or len(answer) >= 2:
        break

    year += 1

print(year) if len(answer) >= 2 else print(0)