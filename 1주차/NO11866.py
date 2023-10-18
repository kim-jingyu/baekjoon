import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
answer = []

queue = [i for i in range(1, N + 1)]
now = 0

while queue:
    now += K - 1
    now %= len(queue)
    answer.append(str(queue.pop(now)))

print('<', ', '.join(answer), '>', sep="")