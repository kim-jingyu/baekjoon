import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = -1e10
min_result = 1e10


def dfs(level, temp_sum):
    global max_result, min_result
    if level == N:
        max_result = max(max_result, temp_sum)
        min_result = min(min_result, temp_sum)
        return

    for i in range(4):
        if operators[i] == 0:
            continue

        operators[i] -= 1
        match i:
            case 0:
                dfs(level + 1, temp_sum + arr[level])
            case 1:
                dfs(level + 1, temp_sum - arr[level])
            case 2:
                dfs(level + 1, temp_sum * arr[level])
            case 3:
                dfs(level + 1, int(temp_sum / arr[level]))
        operators[i] += 1


dfs(1, arr[0])
print(max_result)
print(min_result)
