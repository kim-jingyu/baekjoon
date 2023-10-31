import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:x[0])
meetings.sort(key=lambda x:x[1])

answer = 0
last_end_time = 0

for i in range(len(meetings)):
    start = meetings[i][0]
    end = meetings[i][1]

    if last_end_time <= start:
        last_end_time = end
        answer += 1

print(answer)