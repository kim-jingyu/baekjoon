import sys
input = lambda: sys.stdin.readline().rstrip()

arr = input().split('-')

answer_arr = []

for values in arr:
    value_arr = list(map(int, values.split('+')))
    temp = 0
    for value in value_arr:
        temp += value
    answer_arr.append(temp)

answer = answer_arr[0]

for i in range(1, len(arr)):
    answer -= answer_arr[i]

print(answer)