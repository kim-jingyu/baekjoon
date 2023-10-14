import sys

value = int(sys.stdin.readline().rstrip())

if 90 <= value <= 100:
    print('A')
elif 80 <= value <= 89:
    print('B')
elif 70 <= value <= 79:
    print('C')
elif 60 <= value <= 69:
    print('D')
else:
    print('F')
