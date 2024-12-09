import sys
input = sys.stdin.readline

N = int(input())
my_arr = set(map(int, input().split()))  # 리스트를 집합으로 변환

M = int(input())
serch_arr = list(map(int, input().split()))

# 중복 제거 후 정렬 
sorted_arr = sorted(set(my_arr))

# 기존 정렬과 비교하면서 일치하면 1 아니면 0 넣으면 되나 ? 
result = [1 if num in my_arr else 0 for num in serch_arr]
print(' '.join(map(str, result)))