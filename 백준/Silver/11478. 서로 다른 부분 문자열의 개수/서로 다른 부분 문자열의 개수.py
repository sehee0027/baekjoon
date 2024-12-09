import sys
input = sys.stdin.readline

S = input().strip()
word = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        word.add(S[i:j+1])

print(len(word))