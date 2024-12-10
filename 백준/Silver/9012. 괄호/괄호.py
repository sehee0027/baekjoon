import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().strip()
    stack = []
    is_vps = True

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack: # 스택에 ( 있으면 pop
                stack.pop()
            else: # 스택 비어있으면 VPS 아님 
                is_vps = False
                break

    # 스택이 비어있지 않으면 VPS 아님 
    if stack:
        is_vps = False

    print("YES" if is_vps else "NO")
