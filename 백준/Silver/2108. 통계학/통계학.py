import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 산술평균 
print(round(sum(arr) / n))

# 중앙값 
sort_arr = sorted(arr)
print(sort_arr[n//2])

#최빈값
count = Counter(arr) # 숫자의 빈도 계산 
most_common = count.most_common() # 빈도수가 높은 순서로 정렬된 리스트 반환
max_frequency = most_common[0][1] # 최대 빈도수

fq = [] #최대 빈도수를 가진 수들을 저장하는 리스트
for i in most_common:
    if i[1] == max_frequency: 
        fq.append(i[0])
if len(fq) == 1:            
    print(fq[0])
else:
    print(sorted(fq)[1])

# 범위 
print(max(arr) - min(arr))