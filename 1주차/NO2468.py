# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
import sys

N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_value = 0
for i in range(N):
    for j in range(N):
        max_value = max(board[i][j], max_value)

check_board = [[0]*N for _ in range(N)]

for i in range(max_value):
    pass
