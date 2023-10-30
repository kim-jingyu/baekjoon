import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

objects = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)


for i in range(N):
    weight = objects[i][0]
    value = objects[i][1]

    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[-1])