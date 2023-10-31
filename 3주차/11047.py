import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

values = [int(input()) for _ in range(N)]
values.sort(reverse=True)

answer = 0

for value in values:
    answer += K // value
    K %= value
    if K <= 0:
        break

print(answer)
