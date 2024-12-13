import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(n+1)
visited2 = [0]*(n+1)
result = []
result2 =[]

def dfs(v):
    visited[v] = 1
    result.append(v)
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

def bfs(v):
    queue = [v]
    visited2[v] = 1 
    while queue:
        v = queue.pop(0)
        result2.append(v)
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1
                        
dfs(v)
print(" ".join(map(str, result)))
bfs(v)
print(" ".join(map(str, result2)))
