import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수 

for _ in range(t):
    n, m = map(int, input().split()) # 문서의 개수, 확인할 문서의 위치 
    queue = deque(enumerate(list(map(int, input().split())))) # (인덱스, 중요도)로 저장 
 
    idx = 0 # 출력 순서
    while queue:
        current = queue.popleft() 
        if any(current[1] < doc[1] for doc in queue):
            queue.append(current) # 뒤로 보냄 
        else: # 중요도가 가장 높은 경우
            idx += 1 
            if current[0] == m:
                print(idx)
                break