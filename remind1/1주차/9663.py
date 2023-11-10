import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

result = 0
flag_for_x = [0] * N
flag_for_diagonal_left = [0] * (2 * N - 1)
flag_for_diagonal_right = [0] * (2 * N - 1)


def calculate(y):
    global result
    if y == N:
        result += 1
        return

    for x in range(N):
        if not flag_for_x[x] and not flag_for_diagonal_left[y + x] and not flag_for_diagonal_right[y - x + N - 1]:
            flag_for_x[x] = flag_for_diagonal_left[y + x] = flag_for_diagonal_right[y - x + N - 1] = True
            calculate(y + 1)
            flag_for_x[x] = flag_for_diagonal_left[y + x] = flag_for_diagonal_right[y - x + N - 1] = False


calculate(0)
print(result)