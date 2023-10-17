import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
stack = []
answer = [0] * N

for i in range(len(arr)):
    while stack:
        if stack[-1][1] < arr[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append([i, arr[i]])

print(*answer)
