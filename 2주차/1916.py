import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

INF = int(1e9)


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, end = map(int, input().split())


distance = [INF] * (N + 1)


def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for city_info in graph[now]:
            city, cost = city_info[0], city_info[1],

            cost += dist
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(q, [cost, city])


dijkstra(start)

print(distance[end])