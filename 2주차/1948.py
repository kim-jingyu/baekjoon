import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

time = [0] * (N + 1)
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
back_graph = [[] for _ in range(N + 1)]
cnt = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    back_graph[end].append(start)
    in_degree[end] += 1

source, destination = map(int, input().split())

queue = deque()
queue.append(source)

while queue:
    now = queue.popleft()

    # info[0]: 비용, info[1]: 도시
    for info in graph[now]:
        in_degree[info[1]] -= 1
        # 비용이 갱신될 때
        if time[info[1]] < time[now] + info[0]:
            time[info[1]] = time[now] + info[0]
            # 달려야하는 도로의 수 갱신
            cnt[info[1]] = [now]
        elif time[info[1]] == time[now] + info[0]:
            cnt[info[1]].append(now)

        if in_degree[info[1]] == 0:  # 선행 도로를 모두 지나갔을 때
            queue.append(info[1])

queue = deque([destination])
route = set()
while queue:
    now = queue.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            queue.append(x)

print(time[destination])
print(len(route))
