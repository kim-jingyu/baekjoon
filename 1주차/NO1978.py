import sys
import math


def isprime_number(target):
    for i in range(2, int(math.sqrt(target)) + 1):
        if target % i == 0:
            return False
    return True


if __name__ == '__main__':
    sys.stdin.readline()

    values = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    result = 0
    for value in values:
        if value == 1:
            continue

        if isprime_number(value):
            result += 1

    print(result)
