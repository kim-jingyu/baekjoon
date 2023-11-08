import sys
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
arr = [int(input()) for _ in range(T)]


def is_prime_number(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for now in arr:
    for value in range(now // 2, 1, -1):
        if value == 2:
            print(value, now-value)
            break
        if value % 2 == 0:
            continue
        if is_prime_number(value) and is_prime_number(now-value):
            print(value, now-value)
            break
