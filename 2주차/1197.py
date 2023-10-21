import sys

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())

edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

# Union - Find
root = [i for i in range(V + 1)]


def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x


total_cost = 0


def has_same_root(v1, v2):
    return find(v1) == find(v2)


for edge in edges:
    if has_same_root(edge[0], edge[1]):
        continue
    total_cost += edge[2]
    union(edge[0], edge[1])

print(total_cost)
