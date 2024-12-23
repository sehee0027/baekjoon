import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 1부터 n까지 소수를 판별하기 위한 리스트 
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님 

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(n**0.5) + 1): # √n까지만 탐색
    if is_prime[i]: # i가 소수라면 
        for j in range(i * i, n+1, i): # i의 배수를 False로 
            is_prime[j] = False

# m부터 n까지 소수를 출력 
for i in range(m, n+1):
    if is_prime[i]:
        print(i)