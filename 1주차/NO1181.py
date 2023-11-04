import sys

N = int(sys.stdin.readline().rstrip())
words = set()

for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

new_words = sorted(words, key=lambda w: (len(w), w))

for word in new_words:
    print(word)

