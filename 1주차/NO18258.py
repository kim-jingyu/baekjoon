import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split(' ')
    if len(cmd) == 2:
        queue.appendleft(cmd[1])
        continue
    elif cmd[0] == 'pop':
        if not queue:
            print(-1)
            continue
        print(queue.pop())
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if not queue:
            print(-1)
            continue
        print(queue[-1])
    elif cmd[0] == 'back':
        if not queue:
            print(-1)
            continue
        print(queue[0])
