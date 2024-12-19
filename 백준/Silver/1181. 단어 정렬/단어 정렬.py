import sys
input = sys.stdin.readline

N = int(input())
arr = []
new_arr = []

for _ in range(N):
    arr.append(list(input()))

arr.sort()
arr.sort(key=lambda x: (len(x)))

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

for i in range(len(new_arr)):
    print(''.join(map(str, new_arr[i])), end='')