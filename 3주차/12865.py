# import sys
#
# input = lambda: sys.stdin.readline().rstrip()
#
# N, K = map(int, input().split())
#
# objects = [list(map(int, input().split())) for _ in range(N)]
# dp = [0] * (K + 1)
#
#
# for i in range(N):
#     weight = objects[i][0]
#     value = objects[i][1]
#
#     for j in range(K, weight - 1, -1):
#         dp[j] = max(dp[j], dp[j - weight] + value)
#
# print(dp[-1])

import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

objects = [[0, 0]]
for _ in range(N):
    objects.append(list((map(int, input().split()))))
dp = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = objects[i]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[-1][-1])