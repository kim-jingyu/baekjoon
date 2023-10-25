import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

student_adj_list = [[] for _ in range(N + 1)]
in_degree = [0 for _ in range(N + 1)]
queue = deque()

for i in range(M):
    A, B = map(int, input().split())
    student_adj_list[A].append(B)
    in_degree[B] += 1

# 위상 정렬

# 초기 상태에 진입 차수가 0인 것들을 큐에 넣어준다.
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)


# 해당 정점들과 연결된 정점들의 진입 차수들을 1씩 감소시켜준다. (간선 자르기)
# 해당 노드의 진입 차수가 0이 되면, 큐에 넣어준다.
while queue:
    node = queue.popleft()
    print(node, end=' ')
    for student in student_adj_list[node]:
        in_degree[student] -= 1
        if in_degree[student] == 0:
            queue.append(student)

print()
