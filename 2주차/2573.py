import sys
import copy

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())  # 행, 열

board = [list(map(int, input().split())) for _ in range(N)]
new_board = copy.deepcopy(board)
temp_board = copy.deepcopy(board)

answer = 0
check_global = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


while check_global:
    def remove_part(calc_board, y, x):
        global temp_board
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or ny == N or nx < 0 or nx == M:
                continue

            if calc_board[ny][nx]:
                calc_board[ny][nx] = 0
                remove_part(calc_board, ny, nx)

        temp_board = copy.deepcopy(calc_board)


    def calculate_num_of_lumps(calc_board):
        global answer, check_global
        check = False
        for i in range(N):
            for j in range(M):
                if calc_board[i][j]:
                    check = True
                    calc_board[i][j] = 0
                    answer += 1
                    remove_part(calc_board, i, j)
        check_global = check


    def decrease_iceberg(y, x):
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or ny == N or nx < 0 or nx == M:
                continue

            if new_board[ny][nx] == 0 and temp_board[y][x] > 0:
                temp_board[y][x] -= 1

        calculate_num_of_lumps(temp_board)


    for i in range(N):
        for j in range(M):
            decrease_iceberg(i, j)

print(answer)