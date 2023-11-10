import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

pos = [0] * N
flag_for_y = [False] * N


def put():
    for i in range(N):
        print(f'{pos[i]:2}', end='')  # :2 문자열 자릿수
    print()


def set(i):
    if i == N:
        put()
        return

    for j in range(N):
        if not flag_for_y[j]:
            pos[i] = j
            flag_for_y[j] = True
            set(i + 1)
            flag_for_y[j] = False


set(0)
