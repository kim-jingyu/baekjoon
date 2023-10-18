import sys
import heapq

N = int(sys.stdin.readline().rstrip())
max_heap = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip()) * -1
    if num == 0:
        print(heapq.heappop(max_heap) * -1 if max_heap else 0)
    else:
        heapq.heappush(max_heap, num)
