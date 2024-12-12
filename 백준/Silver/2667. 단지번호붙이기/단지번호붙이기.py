from collections import deque

N = int(input())

# 행렬 만들기
graph = [list(map(int, input())) for _ in range(N)]

def bfs(graph,x,y):
    # 상하좌우 이동 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque() # BFS를 위한 큐 생성
    queue.append((x,y)) # 시작 위치 추가
    graph[x][y] = 0  # 방문한 위치를 0으로 변경 (방문 처리)
    cnt = 1 # 현재 단지 크기 (집의 수)
    
    while queue:
        x,y = queue.popleft() # 현재 위치 꺼내기

        for i in range(4): # 상하좌우로 이동
          nx = x + dx[i]
          ny = y + dy[i]

          # 지도 범위를 벗어나면 무시
          if nx < 0 or nx >= N or ny <0 or ny >= N:
               continue

          # 연결된 집 발견 (방문하지 않은 `1`)     
          if graph[nx][ny] == 1:
               graph[nx][ny] = 0 # 방문 처리
               queue.append((nx,ny)) # 큐에 추가
               cnt += 1 # 단지 크기 증가
    return cnt # 단지 크기 반환

# 단지 크기 계산 
count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

count.sort() # 단지 크기 정렬 
print(len(count)) # 단지 개수 출력

for i in range(len(count)):
    print(count[i]) # 각 단지 크기 출력