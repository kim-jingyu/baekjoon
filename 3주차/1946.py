import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())

    volunteers = [list(map(int, input().split())) for _ in range(N)]
    volunteers.sort()

    now = 0
    answer = 1
    print(volunteers)
    for i in range(1, len(volunteers)):
        if volunteers[i][1] < volunteers[now][1]:
            now = i
            answer += 1

    print(answer)