import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())


def hanoi_top(n, departure, destination):
    if n == 1:
        print(departure, destination)
        return

    hanoi_top(n - 1, departure, 6 - departure - destination)
    print(departure, destination)
    hanoi_top(n - 1, 6 - departure - destination, destination)


print(2**N - 1)


if N < 21:
    hanoi_top(N, 1, 3)
