import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(tickets):
    
    # 티켓 정보를 그래프로 변환 
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 각 공항의 목적지를 사전순으로 정렬 
    for key in graph:
        graph[key].sort(reverse=True)

    stack = ["ICN"] # 출발점 
    path = [] # 여행 경로 

    # DFS
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        path.append(stack.pop())

    return path[::-1]