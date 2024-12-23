## 시간 초과 ## 시간 복잡도: O(M×N)
# n = int(input())
# arr = input().split()

# m = int(input())
# arr2 = input().split()

# result = []
# for i in range(m):
#     if arr2[i] in arr: 
#         result.append(1)
#     else:
#         result.append(0)

# print("\n".join(map(str, result)))

## 집합 사용 ## 
n = int(input())
arr = set(input().split())

m = int(input())
arr2 = input().split()

result = [1 if num in arr else 0 for num in arr2]

print("\n".join(map(str, result)))