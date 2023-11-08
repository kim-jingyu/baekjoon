import sys
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))


def find_prime_number(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


result = 0
for value in arr:
    if value == 1:
        continue

    if find_prime_number(value):
        result += 1

print(result)
