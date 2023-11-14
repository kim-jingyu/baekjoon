import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = set()

for _ in range(N):
    words.add(input())

new_words = sorted(words, key=lambda w: (len(w), w))

for word in new_words:
    print(word)
