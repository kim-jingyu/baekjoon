import sys
import math

T = int(sys.stdin.readline().rstrip())


def is_prime_number(target):
    for x in range(2, int(math.sqrt(target)) + 1):
        if target % x == 0:
            return False
    return True


def when_odd_number():
    global i
    for i in range(n_divided, 2, -2):
        if is_prime_number(i) and is_prime_number(n - i):
            print(f'{i} {n - i}')
            break


def when_even_number():
    global i
    for i in range(n_divided - 1, 2, -2):
        if is_prime_number(i) and is_prime_number(n - i):
            print(f'{i} {n - i}')
            break


if __name__ == '__main__':
    for _ in range(T):
        n = int(sys.stdin.readline().rstrip())
        n_divided = int(n / 2)
        if n_divided == 2:
            print('2 2')
        elif n_divided % 2: # n을 2로 나눈 몫이 홀수이면
            when_odd_number()
        elif not n_divided % 2:
            when_even_number()
