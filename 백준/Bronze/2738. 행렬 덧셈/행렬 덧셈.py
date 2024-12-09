A, B = [], [] 
N, M = map(int, input().split())

for i in range(N):
    num = list(map(int, input().split()))
    A.append(num)

for i in range(N):
    num = list(map(int, input().split()))
    B.append(num)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = ' ')
    print()