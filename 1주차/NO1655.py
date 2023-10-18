import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
max_heap, min_heap = [], []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)  # 최대힙 만들기 (왼쪽)
    else:
        heappush(min_heap, num)  # 최소힙 만들기 (오른쪽)

    if max_heap and min_heap and max_heap[0] * -1 > min_heap[0]:
        max_value = -heappop(max_heap)  # 왼쪽
        min_value = heappop(min_heap)  # 오른쪽

        # swap
        heappush(max_heap, -min_value)
        heappush(min_heap, max_value)

    print(-max_heap[0])