import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [10001 for _ in range(k + 1)]
dp[0] = 0

for i in range(1, k + 1):
    for j in coin:
        if i < j:
            continue
        dp[i] = min(dp[i], dp[i - j] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
