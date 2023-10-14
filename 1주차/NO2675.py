import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    values = sys.stdin.readline().rstrip().split(' ')
    R = int(values[0])
    target = values[1]
    for t in target:
        for _ in range(R):
            print(t, end='')
    print()