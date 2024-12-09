A = [] 

for i in range(9):
    A.append(list(map(int, input().split())))

num = max(list(map(max, A)))
print(num)

for i in range(9):
    for j in range(9):
        if num == A[i][j]:
            print(i+1, j+1, end= ' ')