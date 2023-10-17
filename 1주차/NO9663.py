import sys

N = int(sys.stdin.readline().rstrip())

pos = [0] * N
flag_for_row = [False] * N
flag_for_diagonal_right = [False] * N * 2
flag_for_diagonal_left = [False] * N * 2


def print_row():
    for row in range(8):
        for col in range(8):
            print('👸🏻' if pos[col] == row else '☐', end='')
        print()
    print()


def set(col):
    for row in range(N):
        if not flag_for_row[row] and not flag_for_diagonal_right[row - col + N - 1] and not flag_for_diagonal_left[col + row]:
            pos[col] = row
            if col == N - 1:
                print_row()
            else:
                flag_for_row[row] = flag_for_diagonal_right[row - col + N - 1] = flag_for_diagonal_left[col + row] = True
                set(col + 1)
                flag_for_row[row] = flag_for_diagonal_right[row - col + N - 1] = flag_for_diagonal_left[col + row] = False


set(0)
