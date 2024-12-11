import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    command = input().strip().split()

    if command[0] == '1': # 앞에 추가 
        queue.appendleft(int(command[1]))
    elif command[0] == '2': # 뒤에 추가 
        queue.append(int(command[1]))
    elif command[0] == '3':
        if queue: 
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == '4':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == '5':
        print(len(queue))
    elif command[0] == '6':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == '7':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == '8':
        if queue:
            print(queue[-1])
        else:
            print(-1)