import sys

value = sys.stdin.readline().rstrip()
values = list(map(int, value.split(' ')))

print(values[0] + values[1])
print(values[0] - values[1])
print(values[0] * values[1])
print(int(values[0] / values[1]))
print(values[0] % values[1])
