import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(N))
