import sys

input = lambda: sys.stdin.readline().rstrip()


def top_down(target):
    if target == 0 or target == 1:
        return dp[target]

    if not dp[target]:
        dp[target] = top_down(target - 1) + top_down(target - 2)

    return dp[target]


def bottom_up(target):
    for i in range(2, target + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[target]


n = int(input())
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
print(bottom_up(n))
