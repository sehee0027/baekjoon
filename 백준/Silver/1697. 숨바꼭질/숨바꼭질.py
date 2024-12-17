import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001 # 최대 범위 - 0 ≤ n, k ≤ 100,000 이므로 

def bfs(start, target):
    queue = deque()
    queue.append(start)
    visited[start] = 0 # 시작점 방문 처리

    while queue:
        cur = queue.popleft()

        if cur == target:
            return visited[cur]
        
        for next in (cur - 1, cur + 1, cur * 2):
            if 0 <= next <= 100000 and visited[next] == -1: # 범위 내 & 미방문
                visited[next] = visited[cur] + 1 # 시간 갱신
                queue.append(next) # 큐에 추가

print(bfs(n, k))