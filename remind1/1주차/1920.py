import sys
input = lambda: sys.stdin.readline().rstrip()


def solution(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if answer_arr[mid] == target:
            return 1
        elif answer_arr[mid] > target:
            end = mid - 1
        elif answer_arr[mid] < target:
            start = mid + 1

    return 0


N = int(input())
answer_arr = sorted(list(map(int, input().split())))
M = int(input())
target_arr = list(map(int, input().split()))

for target_value in target_arr:
    print(solution(target_value))