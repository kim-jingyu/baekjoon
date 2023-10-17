import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    temp = sys.stdin.readline().rstrip().split()
    if len(temp) == 2:
        stack.append(int(temp[1]))
        continue
    elif temp[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
    elif temp[0] == 'size':
        print(len(stack))
    elif temp[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'top':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])

