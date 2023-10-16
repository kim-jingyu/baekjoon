# a_n = 2^n - 1
import sys


def print_process(n, start, end):
    if n == 1:
        print(start, end)
        return

    print_process(n - 1, start, 6 - start - end)
    print(start, end)
    print_process(n - 1, 6 - start - end, end)


def move(level, start, target):
    if level > 1:
        move(level - 1, start, 6 - start - target)

    print(f'원반 [{level}]을 {start}기둥에서 {target}기둥으로 옮깁니다.')

    if level > 1:
        move(level - 1, 6 - start - target, target)


value = int(sys.stdin.readline().rstrip())
print(2 ** value - 1)
if value <= 20:
    move(value, 1, 3)
