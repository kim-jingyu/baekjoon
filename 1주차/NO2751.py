import sys

N = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()
for num in nums:
    print(num)
