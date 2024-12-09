import sys
input = sys.stdin.readline

N, M = map(int, input().split())
my_arr = []
search_arr = []

for _ in range(N):
    my_arr.append(input())

for _ in range(M):
    search_arr.append(input())

cnt = 0 
for word in search_arr:
    if word in my_arr:
        cnt += 1 

print(cnt)