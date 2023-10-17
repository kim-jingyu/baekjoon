import sys

N = int(sys.stdin.readline().rstrip())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0


def solution(x, y, width):
    global white, blue
    color = board[x][y]
    for col in range(x, x + width):
        for row in range(y, y + width):
            if color != board[col][row]:
                solution(x, y, width // 2)
                solution(x, y + width // 2, width // 2)
                solution(x + width // 2, y, width // 2)
                solution(x + width // 2, y + width // 2, width // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, N)
print(white)
print(blue)
