import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
# 풍선 번호와 명령 저장 
queue = deque(enumerate(map(int, input().split()), start=1)) 
result = []

while queue: 
    index, step = queue.popleft() # 현재 풍선 번호와 명령어 가져오기 
    result.append(index) # 풍선 터뜨리기 

    if not queue:  # 남은 풍선이 없으면 종료 
        break
      
    # 큐를 step에 맞게 회전 
    if step > 0:
        queue.rotate(-(step-1)) # 오른쪽 이동 
    else:
        queue.rotate(-step)  # 왼쪽 이동 

print(" ".join(map(str, result)))
