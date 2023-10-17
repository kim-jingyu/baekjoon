import sys


def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = int((start + end) / 2)
        if N_arr[mid] == target:
            return True
        elif N_arr[mid] > target:
            end = mid - 1
        elif N_arr[mid] < target:
            start = mid + 1

    return False


N = int(sys.stdin.readline().rstrip())
N_arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
N_arr.sort()
M = int(sys.stdin.readline().rstrip())
M_arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for M in M_arr:
    if binary_search(M):
        print(1)
    else:
        print(0)
