import sys

value = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print(f'{value} * {i} = {value * i}')
