import sys

bucket = []
results = []

for _ in range(9):
    person = int(sys.stdin.readline().rstrip())
    bucket.append(person)


def solution(level, start):
    if level == 7:
        if sum(results) == 100:
            for result in sorted(results):
                print(result)
            exit()
        return

    for i in range(start, len(bucket)):
        results.append(bucket[i])
        solution(level + 1, i + 1)
        results.pop()


solution(0, 0)
print(results)
