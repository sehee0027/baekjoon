N = int(input())
M = int(input())

# 행렬 만들기 
graph = [[0]*(N+1) for _ in range(N+1)] # 정점의 개수만큼 행렬 생성 
for i in range(M): # 정점간의 연결 표시하기 위해 
    a, b = map(int, input().split()) 
    graph[a][b] = graph[b][a] = 1 

# 방문 리스트 행렬
visited = [0]*(N+1)

def dfs(V):
    visited[V] = 1 # 방문 처리 
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)

# 방문한 컴퓨터 수 - 자기 자신(1번 컴퓨터)은 제외
print(sum(visited) - 1)