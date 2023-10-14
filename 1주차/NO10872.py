import sys

target = int(sys.stdin.readline().rstrip())

value = 1
for i in range(1, target + 1):
    value *= i

print(value)
