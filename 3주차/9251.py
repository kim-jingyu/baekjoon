# import sys
#
# input = lambda: sys.stdin.readline().rstrip()
#
# first = input()
# second = input()
# height, width = len(first), len(second)
#
# dp = [[0] * (width + 1) for _ in range(height + 1)]
#
# for i in range(1, height + 1):
#     for j in range(1, width + 1):
#         if first[i - 1] == second[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
#
# print(dp[height][width])
import sys

input = lambda: sys.stdin.readline().rstrip()

word1, word2 = input(), input()
word1_len, word2_len = len(word1), len(word2),
dp = [0] * word2_len

for i in range(word1_len):
    cnt = 0
    for j in range(word2_len):
        if dp[j] > cnt:
            cnt = max(cnt, dp[j])
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1

print(max(dp))


