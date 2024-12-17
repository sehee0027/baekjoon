from collections import deque

def solution(n, computers):
    def bfs(start):
        queue = deque()
        queue.append(start)

        while queue:
            cur = queue.popleft()
            for next in range(n):
                # 연결된 컴퓨터이고 아직 방문하지 않았다면 
                if computers[cur][next] == 1 and not visited[next]:
                    visited[next] = True
                    queue.append(next)

    visited = [0] * n
    cnt = 0 # 네트워크 개수 

    for i in range(n):
        if not visited[i]: # 방문하지 않은 컴퓨터 
            bfs(i)
            cnt += 1 

    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
