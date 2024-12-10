import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []
for _ in range(N):
    command = input().split()

    # 1 X: 정수 X를 스택에 넣는다. 
    if command[0] == '1': 
        stack.append(int(command[1]))

    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == '2': 
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)

    # 3: 스택에 들어있는 정수의 개수를 출력한다.
    elif command[0] == '3': 
        result.append(len(stack))

    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif command[0] == '4': 
        if stack: 
            result.append(0)
        else:
            result.append(1)
            
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == '5':
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))