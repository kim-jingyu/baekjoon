import sys

input = lambda: sys.stdin.readline().rstrip()

dwarfs = [int(input()) for _ in range(9)]
answer = []


def solution(level, start):
    if level == 7:
        if sum(answer) == 100:
            for value in sorted(answer):
                print(value)
            exit()

    for i in range(start, len(dwarfs)):
        answer.append(dwarfs[i])
        solution(level + 1, i + 1)
        answer.pop()


solution(0, 0)
