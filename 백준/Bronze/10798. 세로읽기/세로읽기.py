A = [] 
B = "" # 세로로 읽은 문자열 저장

for i in range(5):
    A.append(list(map(str, input().strip())))

# 가장 긴 문자열의 길이 
max_len = max(len(word) for word in A)

for i in range(max_len):
    for j in range(5):
        if i < len(A[j]):
            B += A[j][i]

print(B)