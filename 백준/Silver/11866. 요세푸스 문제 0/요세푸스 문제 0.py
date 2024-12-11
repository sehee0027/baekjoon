import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
result = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")