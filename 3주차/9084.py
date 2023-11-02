import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)

    for coin in coins:
        if coin > M:
            continue
        dp[coin] += 1
        for i in range(coin, M + 1):
            dp[i] += dp[i-coin]

    print(dp[M])