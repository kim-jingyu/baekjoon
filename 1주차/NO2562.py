import sys

values = []

for _ in range(9):
    value = int(sys.stdin.readline().rstrip())
    values.append(value)

print(max(values))
print(values.index(max(values)) + 1)
