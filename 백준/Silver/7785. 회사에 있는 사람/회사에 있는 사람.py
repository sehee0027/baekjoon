import sys
input = sys.stdin.readline

N = int(input())
temp = dict() # 딕셔너리 형 

for _ in range(N):
    a, b = map(str, input().split())

    # 출입
    if b == 'enter':
        temp[a] = b
    # 퇴근시 삭제 
    else:
        del temp[a]

# 사전 순의 역순으로 정렬 
temp = sorted(temp.keys(), reverse=True)

print("\n".join(temp))