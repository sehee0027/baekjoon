import sys
input = sys.stdin.readline
from collections import deque

def solution(maps):
    n = len(maps) # 행 길이 
    m = len(maps[0]) # 열 길이 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            cur_x, cur_y = queue.popleft() # 현재 위치 꺼냄 

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[cur_x][cur_y] + 1
                    queue.append((nx, ny))
        
        # 거리 반환, 방법 없으면 -1 반환 
        return maps[n - 1][m - 1] if maps[n - 1][m - 1] > 1 else -1 
    return bfs(0, 0)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))