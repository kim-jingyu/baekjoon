import sys

N = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(N):
    nums.append(int(input()))

result = sorted(nums)

for value in result:
    print(value)
