import sys
input = sys.stdin.readline
from collections import deque

n ,m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 시작점 (x, y)를 큐에 추가

    while queue:
        x, y = queue.popleft() # 큐에서 현재 위치를 꺼냄

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 현재 칸의 거리 + 1 기록
                queue.append((nx, ny)) # 이동한 위치를 큐에 추가

    return graph[n-1][m-1]

print(bfs(0, 0))