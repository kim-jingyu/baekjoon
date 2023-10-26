from collections import deque
import heapq
import copy
N, K = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = [list(map(int, input().split())) for i in range(N)]
S, X, Y = map(int, input().split())

heap = []

for i in range(N):
    for j in range(N):
        if graph[i][j]!=0:
            heapq.heappush(heap, (graph[i][j], i, j))
#우선순위는 바이러스 숫자가 작은순
cnt = 0

while cnt != S:
    temp_heap = []
    while heap:
        vi, x, y = heapq.heappop(heap)

        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                graph[nx][ny] = vi
                heapq.heappush(temp_heap, (graph[nx][ny], nx, ny) )
    heap = copy.deepcopy(temp_heap)
    cnt += 1
print(graph[X-1][Y-1])