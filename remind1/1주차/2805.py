import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
tree_arr = list(map(int, input().split()))


def solution():
    start = 0
    end = max(tree_arr)

    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for tree in tree_arr:
            if tree - mid > 0:
                temp += tree - mid
        if temp >= M:
            start = mid + 1  # 잘린 나무의 길이가 너무 길면 시작점 올려주기
        else:
            end = mid - 1  # 잘린 나무의 길이가 부족하면 끝점 아래로 내려주기

    return end


print(solution())
