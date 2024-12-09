import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 집합 연산은 set 자료형 사용 
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B) + len(B-A))