import sys
input = sys.stdin.readline
from collections import deque

def solution(numbers, target):

    def dfs(idx, result):
        if idx == len(numbers): # 숫자 다 사용했을때 
            if result == target: # 합계가 같으면 1 다르면 0 반환 
                return 1 
            else:
                return 0 
            
        add_case = dfs(idx + 1, result + numbers[idx])
        sub_case = dfs(idx + 1, result - numbers[idx])

        return add_case + sub_case
    
    return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1]	, 4))