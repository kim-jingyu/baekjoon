import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heap = [int(input()) for _ in range(N)]


def down_heap(arr, left, right):
    root = arr[left]
    parent = left

    while parent < (right + 1) // 2:
        child_left = parent * 2 + 1
        child_right = child_left + 1

        child = child_right if child_right <= right and arr[child_right] > arr[child_left] else child_left

        if root >= arr[child]:
            break

        arr[parent] = arr[child]
        parent = child

    arr[parent] = root


for i in range((N - 1) // 2, -1, -1):
    down_heap(heap, i, N - 1)

for i in range(N - 1, 0, -1):
    heap[0], heap[i] = heap[i], heap[0],
    down_heap(heap, 0, i - 1)

for value in heap:
    print(value)