import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def solution(x, y, width):
    global white, blue
    color = board[y][x]

    for i in range(y, y + width):
        for j in range(x, x + width):
            if color != board[i][j]:
                solution(x, y, width // 2)
                solution(x, y + (width // 2), width // 2)
                solution(x + (width // 2), y, width // 2)
                solution(x + (width // 2), y + (width // 2), width // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, N)
print(white)
print(blue)