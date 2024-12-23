import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input().strip()))

start = 1 # 최소 길이 
end = max(lines) # 가장 긴 랜선의 길이 

while(start <= end):
    mid = (start + end) // 2 # 자를 길이 
    line_cnt = 0 # 잘라서 얻는 랜선의 개수 

    for line in lines:
        line_cnt += line // mid 

    if line_cnt >= n: # 원하는 개수 이상 만들 수 있다면
        start = mid + 1 # 더 긴 길이를 시도
    else: # 원하는 개수를 만들 수 없다면
        end = mid - 1 # 더 짧은 길이를 시도

print(end) # 랜선의 최대 길이 
