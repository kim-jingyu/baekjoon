# a_n = 2^n - 1
import sys


def print_process(n, start, end):
    if n == 1:
        print(start, end)
        return

    print_process(n - 1, start, 6 - start - end)
    print(start, end)
    print_process(n - 1, 6 - start - end, end)


value = int(sys.stdin.readline().rstrip())
print(2 ** value - 1)
if value <= 20:
    print_process(value, 1, 3)
