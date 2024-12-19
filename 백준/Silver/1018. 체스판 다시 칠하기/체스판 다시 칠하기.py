
n, m = map(int, input().strip().split())
borad = [input().strip() for _ in range(n)]
result = []

# 체스판에서 8×8 크기를 유지
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0 # `B`로 시작하는 체스판의 수정 횟수
        draw2 = 0 # `W`로 시작하는 체스판의 수정 횟수

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 인덱스 (a+b)가 짝수면 B, 홀수면 W
                    if borad[a][b] != 'B':
                        draw1 += 1 
                    if borad[a][b] != 'W':
                        draw2 += 1 
                else:
                    if borad[a][b] != 'W':
                        draw1 += 1 
                    if borad[a][b] != 'B':
                        draw2 += 1 

        result.append(draw1)
        result.append(draw2)

print(min(result))